from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from resources import Episodes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(Episodes, '/episodes')

if __name__ == '__main__':
    app.run(debug=True, port=5555)
