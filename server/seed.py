import random
from datetime import datetime

from app import app
from dateutil.relativedelta import relativedelta
from faker import Faker
from models import Appearance, Episode, Guest, db


def seed_data():
    # Initialize faker
    fake = Faker()

    print('Reseting database...')
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    print('Creating guest objects...')
    for _ in range(50):
        name = fake.unique.name()
        occupation = fake.job()
        guest = Guest(name=name, occupation=occupation)
        db.session.add(guest)
        db.session.commit()
    print('Successfully seeded guests.')

    print('Creating episode objects...')

    # Start date for the episodes
    start_date = datetime(1989, 10, 1)
    for i in range(1, 10 + 1):
        # Increment the date by 1 month for each episode
        date = start_date + relativedelta(months=i)
        date_string = date.strftime('%m/%d/%y')

        # Create a new episode with the incremented date and sequential number
        episode = Episode(date=date_string, number=i)
        db.session.add(episode)
        db.session.commit()
    print('Successfully seeded episodes.')

    print('Creating appearance objects...')
    episodes = Episode.query.all()
    guests = Guest.query.all()
    appearance_set = set()

    while len(appearance_set
              ) < 100:  # Target is to create a 100 unique appearance records
        episode = random.choice(episodes)
        guest = random.choice(guests)
        rating = random.choice(range(1, 5 + 1))

        # Ensure the (episode_id, guest_id) pair is unique
        if (episode.id, guest.id) not in appearance_set:
            # Add the unique pair to the set
            appearance_set.add((episode.id, guest.id))

            # Create the Appearance entry and add to session
            appearance = Appearance(episode_id=episode.id,
                                    guest_id=guest.id,
                                    rating=rating)
            db.session.add(appearance)
    # Commit the session to insert all the uppearance records
    db.session.commit()
    print('Successfully seeded appearances.')


if __name__ == '__main__':
    with app.app_context():
        seed_data()
        print('Complete.')
