from db import db

class Base:
    def save(self):
        db.session.add(self)
        self._commit()
        db.session.refresh(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self.save()

    def delete(self):
        db.session.delete(self)
        self._commit()

    def _commit(self):
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def to_dict(self, whitelist=set(), blacklist=set()):
        attr = self.__dict__.items()
        if whitelist:
            return {k:v for k,v in attr if k in whitelist}
        else:
            blacklist.add('_sa_instance_state')
            return {k:v for k,v in attr if k not in blacklist}
