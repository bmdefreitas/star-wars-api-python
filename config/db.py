import flask_mongoengine

db = flask_mongoengine.MongoEngine()

def initialize_db(app):
    db.init_app(app)
