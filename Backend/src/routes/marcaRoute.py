from models import db
from models.marcaModel import Marca,MarcaSchema
from flask import request
from flask_restful import Resource

marcas_schema=MarcaSchema(many=True)
marca_schema=MarcaSchema()

class MarcasResource(Resource):
    def get(self):
        marcas=Marca.query.all()
        return marcas_schema.dump(marcas)

    def post(self):
        new_marca = Marca(
            idmarca=request.json['idmarca'],
            nommarca=request.json['nommarca'],
        )
        db.session.add(new_marca)
        db.session.commit()
        return marca_schema.dump(new_marca)


class MarcaResource(Resource):
    def get(self, marca_id):
        marca = Marca.query.get_or_404(marca_id)
        return marca_schema.dump(marca)

    def patch(self, marca_id):
        marca = Marca.query.get_or_404(marca_id)

        if 'idmarca' in request.json:
            marca.idmarca = request.json['idmarca']
        if 'nommarca' in request.json:
            marca.nommarca = request.json['nommarca']

        db.session.commit()
        return marca_schema.dump(marca)

    def delete(self, marca_id):
        marca = Marca.query.get_or_404(marca_id)
        db.session.delete(marca)
        db.session.commit()
        return '', 204
