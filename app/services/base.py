from flask_restful import abort

class BaseService:
    def not_found(self, id, name):
        abort(404, message="{} {} não encontrado".format(name, id))