from flask import request
import app.models
from .base import Base

class Crud(Base):

    def index(self, **kwargs):
        page = request.args.get('page', 1)
        per_page = request.args.get('per_page', 50)

        records = self._resource().query
        if request.args.get('order_by'):
            records = self._sort(records)

        data = records.paginate(int(page), int(per_page), False)
        meta = {'total_count': data.total}

        return self._to_json({'data': data.items, 'meta': meta})

    def create(self, **kwargs):
        obj = self._resource()(**request.get_json())
        obj.save()
        if obj.id is None:
            return {'error': 'Something went wrong'}, 422
        return self._to_json(obj), 201

    def show(self, **kwargs):
        obj = self._get_obj(**kwargs)
        return self._to_json(obj)

    def update(self, **kwargs):
        obj = self._get_obj(**kwargs)
        obj.update(**request.get_json())
        return self._to_json(obj)

    def delete(self, **kwargs):
        obj = self._get_obj(**kwargs)
        obj.delete()
        return {}, 204


    def _get_obj(self, **kwargs):
        return self._resource().query.get_or_404(kwargs['id'])

    def _collection(self):
        return self._resource().query.all()

    def _resource(self):
        if not hasattr(self, 'RESOURCE'):
            model_name = self.__module__.split('.')[-1][:-1]
            model = getattr(app.models, model_name.capitalize())
            setattr(self, 'RESOURCE', model)
        return getattr(self, 'RESOURCE')

    def _routes(self):
        if hasattr(self, 'ROUTES'):
            return getattr(self, 'ROUTES')
        else:
            resource_name = self.__module__.split('.')[-1]
            return [
                { 'url': f'/{resource_name}', 'function': 'index' },
                { 'url': f'/{resource_name}', 'function': 'create' },
                { 'url': f'/{resource_name}/<id>', 'function': 'show' },
                { 'url': f'/{resource_name}/<id>', 'function': 'update' },
                { 'url': f'/{resource_name}/<id>', 'function': 'delete' }]

    def _sort(self, data):
        order_by = request.args.get('order_by')
        order_column = getattr(self._resource(), order_by)

        if order_column is None:
            return data

        if request.args.get('order', 'ASC').lower() == 'asc':
            data = data.order_by( order_column.asc() )
        else:
            data = data.order_by( order_column.desc() )

        return data
