import os 
from dotenv import load_dotenv #variables de entorno
from flask import Flask
from flask_restful import Api #para crear la api-rest


api = Api()


def create_app():

    app = Flask(__name__)

    load_dotenv()

    import main.resources as resources
    api.add_resource(resources.ClientesResource, '/clientes')
    api.add_resource(resources.ClienteResource, '/clientes/<id>' )

    api.init_app(app)

    return app