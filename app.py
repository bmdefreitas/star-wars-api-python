from flask import Flask
from flask_restful import Api
from config.db import initialize_db
from routes.planetas import routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/starwars'
}

initialize_db(app)


routes(api)


if __name__ == "__main__":
    app.run(debub=True)
