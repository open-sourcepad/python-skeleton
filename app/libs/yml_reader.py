import yaml

class YamlReader:
    def __init__(self, **kwargs):
        self.file = kwargs.get('file')

    def read(self):
        with open(self.file) as stream:
            try:
                return yaml.safe_load(stream)
            except Exception as e:
                return {}
