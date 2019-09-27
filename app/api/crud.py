from flask import request
import app.models
from .base import Base

class Crud(Base):

    def index(self, **kwargs):
        return self._to_json(self._collection())

    def create(self, **kwargs):
        obj = self._resource()(**request.get_json())
        obj.save()
        if obj.id is None:
            return {'error': 'Something went wrong'}, 422
        return self._to_json(obj), 201

    def show(self, **kwargs):
        obj = self._get_obj()
        return self._to_json(obj)

    def update(self, **kwargs):
        obj = self._get_obj()
        obj.update(**request.get_json())
        return self._to_json(obj)

    def delete(self, **kwargs):
        obj = self._get_obj()
        obj.delete()
        return {}, 204


    def _get_obj(self):
        return self._resource().query.get_or_404(kwargs['id'])

    def _collection(self):
        return self._resource().query.all()

    def _resource(self):
        if not hasattr(self, 'RESOURCE'):
            model_name = self.__module__.split('.')[-1][:-1]
            model = getattr(app.models, model_name.capitalize())
            setattr(self, 'RESOURCE', model)
        return getattr(self, 'RESOURCE')

    # def _paginate(self, data, params):
        # data.__class__ = BaseQuery

        # page, per_page = params.get('page', 1), params.get('per_page', 50)
        # pagination = data.paginate(int(page), int(per_page), False)

        # return pagination.items, pagination

    # def _sort(self, data, params, mapping):
        # order_by = params.get('order_by')
        # order_column = mapping.get(order_by)

        # if order_column is None:
            # return data

        # if type(order_column) is str:
            # if params.get('order', 'ASC').lower() == 'asc':
                # data = data.order_by( text(f'{order_column} ASC') )
            # else:
                # data = data.order_by( text(f'{order_column} DESC') )
        # else:
            # if params.get('order', 'ASC').lower() == 'asc':
                # data = data.order_by( order_column.asc() )
            # else:
                # data = data.order_by( order_column.desc() )

        # return data
