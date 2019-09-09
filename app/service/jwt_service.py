import json, os

from jwt import(
    JWT,
    jwk_from_pem
)

class JwtService:
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        self.certificate = os.path.abspath(os.path.abspath(os.path.join('jwt_key.pem')))
        self.engine = JWT()
        self.encoding = 'RS256'

    def encode(self):
        try:
            return self.engine.encode(self.data, self._signing_key_pem(), self.encoding)
        except Exception as e:
            return {
                'error': True,
                'message': e.__str__()
            }

    def decode(self):
        try:
            return self.engine.decode(self.data, self._signing_key_pem())
        except Exception as e:
            return {
                'error': True,
                'message': e.__str__()
            }

    def _signing_key_pem(self):
        key = None
        with open(self.certificate, 'rb') as fh:
            key = jwk_from_pem(fh.read())

        return key
