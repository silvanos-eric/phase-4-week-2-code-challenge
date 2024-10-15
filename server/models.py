from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    number = db.Column(db.Integer)


class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    episode_id = db.Column(db.Integer,
                           db.ForeignKey('episodes.id'),
                           nullable=False)
    guest_id = db.Column(db.Integer,
                         db.ForeignKey('guests.id'),
                         db.ForeignKey('guests.id'),
                         nullable=False)

    __table_args__ = UniqueConstraint('episode_id',
                                      'guest_id',
                                      name='uq_episode_id_guest_id'),


class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)
