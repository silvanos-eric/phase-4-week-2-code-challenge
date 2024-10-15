from sqlite3 import Connection

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event, func
from sqlalchemy.engine import Engine
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, _):
    """
    Enable foreign key constraints on the database connections.
    """
    if not isinstance(dbapi_connection, Connection):
        return

    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, server_default=func.now())
    number = db.Column(db.Integer)

    appearances = db.relationship('Appearance',
                                  backref='episode',
                                  cascade='all, delete-orphan')
    guests = association_proxy('appearances', 'guest')


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

    serialize_rules = '-episode.appearances', '-guest.appearances'


class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    appearances = db.relationship('Appearance',
                                  backref='guest',
                                  cascade='all, delete-orphan')
    episodes = association_proxy('appearances', 'episode')
