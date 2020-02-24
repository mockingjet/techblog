from db import db


class Base(db.Model):
    __abstract__ = True

    def as_dict(self):
        self_dict = {}
        for col, val in self.__dict__.items():
            if not col.startswith('_'):
                self_dict.update({col: val})
        return self_dict

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
