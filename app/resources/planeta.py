from flask import request
from flask_restful import Resource
from app.services.planeta import PlanetaService

class PlanetaResource(Resource):
    def get(self, id):
        return PlanetaService().show(id)

    def put(self, id):
        planeta = request.get_json()
        return PlanetaService().update(id, planeta)

    def delete(self, id):
        return PlanetaService().remove(id)

class PlanetaListResource(Resource):
    def get(self):
        return PlanetaService().index()

    def post(self):
        planeta = request.get_json()
        return PlanetaService().create(planeta)

class PlanetaSearchResource(Resource):
    def get(self):
        nome = request.args.get("nome")
        return PlanetaService().search(nome)