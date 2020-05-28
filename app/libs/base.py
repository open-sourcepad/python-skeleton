from .logger import Logger

class Base:
    def __init__(self, *args, **kwargs):
        self.type = kwargs.get('type', 'info')
        self.file = kwargs.get('file', 'app')
        self.message = kwargs.get('message')

    def log_info(self, message=None):
        if message is not None:
            self.message = message
        self._logger()

    def log_error(self, message=None):
        if message is not None:
            self.message = message

        message = "Error occurred {error}".format(error=self.message)
        self.message = message
        self.type = 'error'
        if self.file == 'app':
            self.file = 'app_error'

        self._logger()

    def _logger(self):
        Logger(
            message=self.message,
            file=self.file,
            type=self.type
        ).log()


class ExceptionBase(Base, Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_error(message=args[0])
