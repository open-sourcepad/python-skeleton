from app.api.home import Home
from conf.config import METHOD_DEFAULTS
class Routes:

    def __init__(self, instance):
        self.instance = instance
        self.classes = self._cls()

    def add_routes(self):
        for cls in self.classes:
            cls_instance = cls()
            for route in cls.ROUTES:
                attr = getattr(cls_instance, route['function'], None)
                if attr:
                    checker = self._checker(route['function'])
                    options = { 'methods': ['GET'] }
                    if checker:
                        options = checker

                    if 'kwargs' in route.keys():
                        options = route['kwargs']

                    self.instance.add_url_rule(
                        route['url'],
                        route['name'],
                        attr,
                        **options
                    )

    def _checker(self, function):
        if function in self._defaults().keys():
            return self._defaults()[function]

        return False

    def _defaults(self):
        return METHOD_DEFAULTS

    def _cls(self):
        return [
            Home
        ]
