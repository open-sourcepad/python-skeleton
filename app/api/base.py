import simplejson as json
from flask import request

class Base:

    @property
    def params(self):
        params = {}
        params = dict(request.args)

        if params == {}:
            for f in [
                'params_json',
                'params_data'
            ]:
                attr = getattr(self, f, None)
                if attr:
                    params = attr

                    if params != {}: break

        return params

    @property
    def raw_params(self):
        return request

    @property
    def params_json(self):
        json_data = getattr(request, 'get_json', None)
        params = {}
        if json_data != {}: params = json_data()

        return params

    @property
    def params_data(self):
        data = getattr(request, 'get_data', None)
        new_data = None
        params = {}

        if data != {}: new_data = data()
        if new_data is not None: params = json.loads(new_data.decode('utf8'))

        return params

    def _to_json(self, data):
        return json.dumps(self._deep_to_dict(data), use_decimal=True, default=str)

    def _deep_to_dict(self, data):
        result = data

        if hasattr(data, 'to_dict'):
            result = data.to_dict()
        elif type(data) is dict:
            result = {}
            for key, val in data.items():
                result[key] = self._deep_to_dict(val)
        elif type(data) in (list, set, tuple):
            result = []
            for val in data:
                result.append(self._deep_to_dict(val))

        return result


    def _routes(self):
        return getattr(self, 'ROUTES', [])
