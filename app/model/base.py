from conf.database import db_session
from sqlalchemy.ext.declarative import declarative_base

BaseDeclaration = declarative_base()
BaseDeclaration.query = db_session.query_property()

def init_db():
    from user import User
    Base.metadata.create_all(bind=engine)

class BaseModel:

    def to_dict(self, **kwargs):
        serializable = False
        if 'serializable' in kwargs.keys() and kwargs['serializable']:
            serializable = True

        return self.to_dict_except({'_sa_instance_state'}, serializable=serializable)

    def to_dict_except(self, keys = {}, serializable=False):
        raw_data = {}

        if serializable:
            raw_data = self.serialize(self.__dict__)
        else:
            raw_data = self.__dict__

        return { x: raw_data[x] for x in raw_data if x not in keys }

    def serialize(self, dict):
        for k,v in dict.items():
            if type(v) != str:
                dict[k] = str(dict[k])

        return dict
