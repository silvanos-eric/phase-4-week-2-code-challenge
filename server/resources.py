from flask import jsonify
from flask_restful import Resource
from models import Episode, Guest, db


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
        errors = []

        try:
            if not episode:
                raise ValueError(f'Episode with ID {id} does not exist')

            episode_dict = episode.to_dict(rules=('-appearances.episode', ))

            return episode_dict
        except ValueError as e:
            errors.append(str(e))
            return {'errors': errors}


class Appearances(Resource):
    pass


class Guests(Resource):

    def get(self):
        guest_list = Guest.query.all()

        guest_dict_list = [
            guest.to_dict(rules=('-appearances', )) for guest in guest_list
        ]

        return guest_dict_list
