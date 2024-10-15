from datetime import datetime, timedelta

from app import app
from faker import Faker
from models import Episode, Guest, db


def seed_data():
    # Initialize faker
    fake = Faker()

    print('Deleting existing guests...')
    Guest.query.delete()
    print('Creating guest objects...')
    guests = []
    for _ in range(50):
        name = fake.unique.name()
        occupation = fake.job()
        guest = Guest(name=name, occupation=occupation)
        guests.append(guest)
        db.session.add(guest)
        db.session.commit()
    print('Successfully created guests.')

    print('Deleting existing episodes...')
    Episode.query.delete()
    print('Creating episode objects...')
    episodes = []
    # Start date for the episodes
    start_date = datetime.now()
    for i in range(1, 10 + 1):
        # Increment the date by 7 days for each episode
        date = start_date + timedelta(days=(i - 1) * 7)
        # Create a new episode with the incremented date and sequential number
        episode = Episode(date=date, number=i)
        episodes.append(episode)
        db.session.add(episode)
        db.session.commit()
    print('Successfully created episodes.')


if __name__ == '__main__':
    with app.app_context():
        seed_data()
        print('Complete.')
