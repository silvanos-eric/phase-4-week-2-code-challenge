# phase-4-week-2-code-challenge

## Flask API with Episodes, Guests, and Appearances

This is a simple Flask-based API that manages episodes, guests, and their appearances on different episodes. It uses SQLite as the database and includes features such as database migrations, RESTful routes, and a seeding mechanism to populate the database with test data.

## Features

- Flask with SQLAlchemy ORM for database management
- Flask-Migrate for database migrations
- Flask-RESTful for building REST APIs
- Seeding script to populate the database with sample data
- Alembic for managing database migrations

## Project Structure

```bash
.
├── .gitignore
├── LICENSE
├── Pipfile
├── README.md
└── server
    ├── app.py
    ├── debug.py
    ├── instance
    │   └── app.db
    ├── migrations
    │   ├── alembic.ini
    │   ├── env.py
    │   ├── README
    │   ├── script.py.mako
    │   └── versions
    │       └── 91b5c5c800fd_initial_migration.py
    ├── models.py
    ├── resources.py
    └── seed.py
```

## Setup Instructions

### Prerequisites

- Python 3.12.x
- [Pipenv](https://pipenv.pypa.io/en/latest/) for managing dependencies.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install dependencies using Pipenv:

   ```bash
   pipenv install --dev
   ```

3. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

4. Run migrations to set up the database:

   ```bash
   cd server
   flask db upgrade
   ```

5. Seed the database with sample data (make sure you are inside the `server` directory):

   ```bash
   python seed.py
   ```

### Running the Application

To start the Flask development server, run (from inside `server` directory):

```bash
python app.py
```

Alternatively if you prefer using the `Flask CLI`

```bash
flask run
```

The API will be available at `http://127.0.0.1:5555`.

### API Endpoints

- **GET /episodes** - Fetch all episodes.
- **GET /episodes/<id>** - Fetch a specific episode by ID.
- **POST /appearances** - Create a new appearance.
- **GET /guests** - Fetch all guests.

### Database Migrations

To create a new migration after making changes to the models, run (from inside `server` directory):

```bash
flask db migrate -m "Migration message"
flask db upgrade
```

### Debugging

For debugging, you can use the `server/debug.py` file:

```bash
python debug.py
```

This will launch an interactive debugging session.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **Your Name** - _Initial work_
