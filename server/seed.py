from app import app
from faker import Faker
from models import Guest, db


def seed_data():
    # Initialize faker
    fake = Faker()
    print('Deleting existing guests...')
    Guest.query.delete()

    print('Creating guest objects...')
    guests = []
    for _ in range(20):
        name = fake.unique.name()
        occupation = fake.job()
        guest = Guest(name=name, occupation=occupation)
        guests.append(guest)
        db.session.add(guest)
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed_data()
        print('Complete.')
