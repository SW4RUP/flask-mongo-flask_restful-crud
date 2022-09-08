from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config.from_envvar('ENV_FILE_LOCATION')

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/moviebag'
}

initialize_db(app)
initialize_routes(api)

app.run()