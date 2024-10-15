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

To start the Flask development server, run:

```bash
python server/app.py
```

The API will be available at `http://127.0.0.1:5555`.

### API Endpoints and Example Responses

#### **GET /episodes**

Fetch all episodes.

**Request:**

```bash
curl -X GET http://127.0.0.1:5555/episodes
```

**Response:**

```json
[
    {
        "id": 1,
        "date": "10/01/89",
        "number": 1
    },
    {
        "id": 2,
        "date": "11/01/89",
        "number": 2
    }
    ...
]
```

#### **GET /episodes/&lt;id&gt;**

Fetch a specific episode by ID.

**Request:**

```bash
curl -X GET http://127.0.0.1:5555/episodes/1
```

**Response:**

```json
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1,
    "appearances": [
        {
            "episode_id": 1,
            "guest": {
                "id": 1,
                "name": "Michael J. Fox",
                "occupation": "actor"
            },
            "guest_id": 1,
            "id": 1,
            "rating": 4
        }
    ]
}
```

#### **POST /appearances**

Create a new appearance by submitting JSON data.

**Request:**

```bash
curl -X POST http://127.0.0.1:5555/appearances \
-H "Content-Type: application/json" \
-d '{
    "rating": 5,
    "episode_id": 1,
    "guest_id": 1
}'
```

**Response:**

```json
{
  "rating": 5,
  "episode_id": 100,
  "guest_id": 123
}
```

**Error Example (Duplicate Appearance):**

```json
{
    "errors": [
        "Duplicate Appearance. Appearance already exists"
    ]
}
```

#### **GET /guests**

Fetch all guests.

**Request:**

```bash
curl -X GET http://127.0.0.1:5555/guests
```

**Response:**

```json
[
    {
        "id": 1,
        "name": "John Doe",
        "occupation": "Comedian"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "occupation": "Actor"
    }
]
```

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
