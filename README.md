# Star Wars API [![Build Status](https://travis-ci.com/bmdefreitas/star-wars-api-python.svg?branch=master)](https://travis-ci.com/bmdefreitas/star-wars-api-python)
Stat Wars API - Python com Flask

## Iniciando com Docker

Clonar o repositório

```
git clone https://github.com/bmdefreitas/star-wars-api-python.git
```

Iniciando com docker compose

```
docker-compose up
```


## Iniciando sem Docker

Clonar o repositório

```
git clone https://github.com/bmdefreitas/star-wars-api-python.git
```

Instalar as dependências

```
pip install pipenv
pipenv install
```

*Antes de iniciar a API se faz necessário uma instância de mongo configurada. Caso tenha um mongodb em localhost, nada precisa ser configurado.


Inciando em modo DEV

```
FLASK_APP=app/app.py FLASK_ENV=development flask run
```

## Testando

Testando a API

```
pytest -v -s tests
```

## Rotas

```
GET    http://localhost:5000/api/v1/planetas
GET    http://localhost:5000/api/v1/planetas/1
GET    http://localhost:5000/api/v1/planetas/search?nome=Planeta
POST   http://localhost:5000/api/v1/planetas
PUT    http://localhost:5000/api/v1/planetas/1
DELETE http://localhost:5000/api/v1/planetas/1
```


## Documentação

Gerando a documentação

```
pipenv run docs
```
