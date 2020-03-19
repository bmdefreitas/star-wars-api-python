from resources.planeta import PlanetaListResource, PlanetaSearchResource, PlanetaResource

def routes(api):
    api.add_resource(PlanetaListResource, '/api/v1/planetas')
    api.add_resource(PlanetaSearchResource, '/api/v1/planetas/search')
    api.add_resource(PlanetaResource, '/api/v1/planetas/<id>')