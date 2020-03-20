import requests
from .base import BaseService

class SwapiService(BaseService):
  def __init__(self):
    self.urlApi = 'https://swapi.co/api/'

  def findByName(self, name):
    response = requests.get("{}planets?search={}".format(self.urlApi, name))
    return response.json()


  def getQtdeAparicoesFilmes(self, name):
    response = self.findByName(name)
    planeta = '' if response['count'] <= 0 else response['results'][0]
    return 0 if planeta == '' else planeta['films'].__len__()