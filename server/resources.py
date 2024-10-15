from flask import jsonify
from flask_restful import Resource
from models import Episode, db


class Episodes(Resource):

    def get(self):
        episode_list = Episode.query.all()
        episode_dict_list = [
            episode.to_dict(rules=('-appearances', ))
            for episode in episode_list
        ]
        return episode_dict_list


class EpisodeByID(Resource):

    def get(self, id):
        episode = db.session.get(Episode, id)
        episode_dict = episode.to_dict(rules=('-appearances.episode', ))
        return episode_dict


class Appearances(Resource):
    pass


class Guests(Resource):
    pass
