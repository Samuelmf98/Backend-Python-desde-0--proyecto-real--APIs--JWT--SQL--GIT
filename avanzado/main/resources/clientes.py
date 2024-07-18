from flask_restful import Resource
from flask import jsonify, request

clientes = [

    {
        "id": 1,
        "nombre": "samuel",
        "apelido": "marcos"
    },

    {
        "id": 2,
        "nombre": "ganesha",
        "apellido": "gonzalez"
    }

]

class Clientes(Resource):

    def get(self):

        return jsonify(
            {
                "clientes": clientes
        }
        )
    
    def post(self):

        cliente = request.get_json()
        if not cliente:
            return {"message": "Datos de cliente no proporcionados"}, 400
        clientes.append(cliente)
        return cliente, 201

class Cliente(Resource):

    def get(self, id):
        
        for cliente in clientes:
            if cliente["id"] == int(id):


                return jsonify(
                    {
                        "clientes": cliente
                }
                )
    def delete(self, id):

        cliente = request.get_json()
        if not cliente:
            return {"message": "Datos de cliente no proporcionados"}, 400
        for i, cliente in enumerate(clientes):
            if cliente["id"] == int(id):
                clientes.pop(i)
                return cliente, 201



