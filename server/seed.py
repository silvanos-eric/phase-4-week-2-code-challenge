import random
from datetime import datetime

from app import app
from dateutil.relativedelta import relativedelta
from faker import Faker
from models import Appearance, Episode, Guest, db


def seed_data():
    """
    This function seeds the database with random data. Specifically, it resets the
    database, creates 50 guests, 100 episodes, and 150 appearances. The appearances
    are randomly assigned to guests and episodes. The episodes have a sequential
    number and a date that increments by 1 month starting from Oct 1, 1989.

    The function uses the Faker library to generate fake data. The appearances are
    stored in a set to ensure that the (episode_id, guest_id) pair is unique. The
    seed data is then committed to the database.

    :return: None
    """
    # Initialize faker
    fake = Faker()
    print('Reseting database...')
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    number_of_guests = 50
    number_of_episodes = 100
    number_of_appearances = 150

    print(f'Creating {number_of_guests} guests...')
    for _ in range(50):
        name = fake.unique.name()
        occupation = fake.job()
        guest = Guest(name=name, occupation=occupation)
        db.session.add(guest)
        db.session.commit()
    print(f'Successfully seeded {number_of_guests} guests.')

    print(f'Creating {number_of_episodes} episodes...')
    # Start date for the episodes
    start_date = datetime(1989, 10, 1)
    for i in range(number_of_episodes):
        # Increment the date by 1 month for each episode
        date = start_date + relativedelta(months=i)
        date_string = date.strftime('%m/%d/%y')

        # Create a new episode with the incremented date and sequential number
        episode = Episode(date=date_string, number=i + 1)
        db.session.add(episode)
        db.session.commit()
    print(f'Successfully seeded {number_of_episodes} episodes.')

    print(f'Creating {number_of_appearances} appearances...')
    episodes = Episode.query.all()
    guests = Guest.query.all()
    appearance_set = set()

    while len(
            appearance_set
    ) < number_of_appearances:  # Target is to create a 100 unique appearance records
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
    print(f'Successfully seeded {number_of_appearances} appearances.')


if __name__ == '__main__':
    with app.app_context():
        seed_data()
        print('Complete.')
