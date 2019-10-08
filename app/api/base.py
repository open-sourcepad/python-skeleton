import simplejson as json

class Base:

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
