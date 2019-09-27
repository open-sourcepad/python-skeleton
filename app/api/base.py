import simplejson as json

class Base:

    def _to_json(self, data):
        to_dump = data
        if type(data) is list:
            to_dump = [x.to_dict() for x in data]
        elif hasattr(data, 'to_dict'):
            to_dump = data.to_dict()
        return json.dumps(to_dump, use_decimal=True, default=str)
