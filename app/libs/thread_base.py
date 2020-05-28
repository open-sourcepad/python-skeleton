from .base import Base
from threading import Thread


class ThreadBaseError(Exception):
    pass

class ThreadBase(Base):
    def __init__(self, **kwargs):
        self.thread = Thread(target=self.perform, kwargs=kwargs)
        super().__init__(**kwargs)

    def run(self):
        try:
            self.thread.start()
            return self.thread
        except Exception as e:
            self.log_error(message=str(e.__class__))
            raise ThreadBaseError(
                f"Error process initialization.\nError: {e}",
                file='thread_error'
            )
