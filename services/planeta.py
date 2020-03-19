from flask import Response, request
from models.planeta import Planeta
from .base import BaseService
from .swapi import SwapiService


class PlanetaService(BaseService):
    def __init__(self):
        super()

    def index(self):
        try:
            planetas = Planeta.objects().to_json()
            return Response(planetas, mimetype="application/json", status=200)
        except:
            return Response('', mimetype="application/json", status=500)

    def show(self, id):
        try:
            planeta = Planeta.objects.get(id=id).to_json()
            return Response(planeta, mimetype="application/json", status=200)
        except:
            self.not_found(id, 'Planeta')

    def search(self, name):
        try:
            planeta = Planeta.objects(nome__icontains=name).to_json()
            return Response(planeta, mimetype="application/json", status=200)
        except:
            return Response('', mimetype="application/json", status=500)

    def create(self, planeta):
        try:
            planeta['qtdeAparicoesFilmes'] = SwapiService().getQtdeAparicoesFilmes(planeta['nome']);
            planetaCriado = Planeta(**planeta).save().to_json()
            return Response(planetaCriado, mimetype="application/json", status=201)
        except:
            return Response('', mimetype="application/json", status=500)

    def update(self, id, planeta):
        try:
            Planeta.objects.get(id=id).update(**planeta)
            return Response(Planeta.objects.get(id=id).to_json(), mimetype="application/json", status=200)
        except:
            self.not_found(id, 'Planeta')

    def remove(self, id):
        try:
            Planeta.objects.get(id=id).delete()
            return Response('', mimetype="application/json", status=204)
        except:
            self.not_found(id, 'Planeta')
