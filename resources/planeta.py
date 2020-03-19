from flask import Response, request
from flask_restful import abort, Resource
from models.planeta import Planeta
from services.swapi import SwapiService
from services.planeta import PlanetaService

# def not_found(id, name = "Planeta"):
#     abort(404, message="{} {} não encontrado".format(name, id))

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

# class PlanetaResource(Resource):
#     def get(self, id):
#         try:
#             planeta = Planeta.objects.get(id=id).to_json()
#             return Response(planeta, mimetype="application/json", status=200)
#         except:
#             not_found(id)
#
#     def put(self, id):
#         try:
#             body = request.get_json()
#             planeta = Planeta.objects.get(id=id)
#             planeta.update(**body)
#             return Response(Planeta.objects.get(id=id).to_json(), mimetype="application/json", status=200)
#         except:
#             not_found(id)
#
#     def delete(self, id):
#         try:
#             Planeta.objects.get(id=id).delete()
#             return Response('', mimetype="application/json", status=204)
#         except:
#             not_found(id)
#
# class PlanetaListResource(Resource):
#     def get(self):
#         try:
#             planetas = Planeta.objects().to_json()
#             return Response(planetas, mimetype="application/json", status=200)
#         except:
#             return Response('', mimetype="application/json", status=500)
#
#     def post(self):
#         try:
#             body = request.get_json()
#             body["qtdeAparicoesFilmes"] = SwapiService().getQtdeAparicoesFilmes(body["nome"])
#             planeta = Planeta(**body).save().to_json()
#             return Response(planeta, mimetype="application/json", status=201)
#         except NameError:
#             return Response('', mimetype="application/json", status=500)
#
# class PlanetaSearchResource(Resource):
#     def get(self):
#         try:
#             nome = request.args.get("nome");
#             planeta = Planeta.objects(nome__icontains=nome).to_json()
#             return Response(planeta, mimetype="application/json", status=200)
#         except:
#             return Response('', mimetype="application/json", status=500)