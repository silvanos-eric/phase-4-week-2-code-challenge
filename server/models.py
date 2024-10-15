from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Episode(db.Model, SerializerMixin):
    pass


class Appearance(db.Model, SerializerMixin):
    pass


class Guest(db.Model, SerializerMixin):
    pass
