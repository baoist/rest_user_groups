from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from collections import OrderedDict
from sqlalchemy import Column

db = SQLAlchemy()


class DictSerializableMixin(object):
    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result


class User(db.Model, DictSerializableMixin):
    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    first_name = Column(db.String)
    last_name = Column(db.String)
    userid = Column(db.String, unique=True)
    group_id = Column(db.Integer, db.ForeignKey('groups.id'))
    group = relationship("Group", back_populates="users")

    def __init__(self, first_name, last_name, userid):
        self.first_name = first_name
        self.last_name = last_name
        self.userid = userid


class Group(db.Model, DictSerializableMixin):
    __tablename__ = 'groups'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    users = relationship('User', backref='groups', lazy='dynamic')

    def __init__(self, name):
        self.name = name
