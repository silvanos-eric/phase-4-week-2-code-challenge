from flask import request
from flask_restful import Resource
from models import Appearance, Episode, Guest, db
from sqlalchemy.exc import IntegrityError


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

    def post(self):
        data = request.json
        errors = []

        try:
            rating = data['rating']
            episode_id = data['episode_id']
            guest_id = data['guest_id']

            episode = db.session.get(Episode, episode_id)
            guest = db.session.get(Guest, guest_id)

            if not episode:
                raise ValueError('Invalid episode_id')
            if not guest:
                raise ValueError('Invalid guest_id')

            new_appearance = Appearance(guest_id=guest_id,
                                        episode_id=episode_id,
                                        rating=rating)
            db.session.add(new_appearance)
            db.session.commit()

            new_appearance_dict = new_appearance.to_dict()

            return new_appearance_dict, 201
        except KeyError as e:
            errors.append(f'Missing required field: {e}')
        except ValueError as e:
            errors.append(str(e))
        except IntegrityError as e:
            if 'UNIQUE' in str(e):
                errors.append(
                    f'Duplicate Appearance. Appearance already exists')
        return {'errors': errors}


class Guests(Resource):

    def get(self):
        guest_list = Guest.query.all()

        guest_dict_list = [
            guest.to_dict(rules=('-appearances', )) for guest in guest_list
        ]

        return guest_dict_list
