from config.db import db

class Planeta(db.Document):
    nome = db.StringField(required=True, unique=True)
    clima = db.StringField(required=True)
    terreno = db.StringField(required=True)
    qtdeAparicoesFilmes = db.IntField(required=True)
    meta = {'collection': 'planetas'}
