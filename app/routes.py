from app.api.home import Home

class Routes:

    def __init__(self, instance):
        self.instance = instance
        self.classes = self._cls()

    def add_routes(self):
        for cls in self.classes:
            for route in cls.ROUTES:
                attr = getattr(cls(), route['function'], None)
                methods = ['GET']
                if attr:
                    self.instance.add_url_rule(
                        route['url'],
                        route['name'],
                        attr,
                        **route['kwargs']
                    )

    def _cls(self):
        return [
            Home
        ]
