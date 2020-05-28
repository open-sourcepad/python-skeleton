from .base import Base, ExceptionBase
from multiprocessing import Process

class ProcessBaseError(ExceptionBase):
        pass

class ProcessBase(Base):
    def __init__(self, **kwargs):
        self.process = Process(target=self.perform, kwargs=kwargs)
        super().__init__(**kwargs)

    def run(self):
        try:
            self.process.start()
            return self.process
        except Exception as e:
            raise ProcessBaseError(
                f"Error process initialization.\nError: {e}",
                file='process_error'
            )
