from flask import jsonify
from .base import Base

class BaseApi(Base):

    def on(self, response, code):
        return self.json_response(response), code
