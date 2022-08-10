from models import db
from models.espacioModel import Espacio,EspacioSchema
from flask import request
from flask_restful import Resource

espacios_schema=EspacioSchema(many=True)
espacio_schema=EspacioSchema()

class EspaciosResource(Resource):
    def get(self):
        espacios=Espacio.query.all()
        return espacios_schema.dump(espacios)

    def post(self):
        new_espacio = Espacio(
            codespacio=request.json['codespacio'],
            idtipoespacio_espacio=request.json['idtipoespacio_espacio'],
            codespacio_espacio=request.json['codespacio_espacio'],
            nomespacio=request.json['nomespacio'],
        )
        db.session.add(new_espacio)
        db.session.commit()
        return espacio_schema.dump(new_espacio)


class EspacioResource(Resource):
    def get(self, espacio_id):
        espacio = Espacio.query.get_or_404(espacio_id)
        return espacio_schema.dump(espacio)

    def patch(self, espacio_id):
        espacio = Espacio.query.get_or_404(espacio_id)

        if 'codespacio' in request.json:
            espacio.codespacio = request.json['codespacio']
        if 'idtipoespacio_espacio' in request.json:
            espacio.idtipoespacio_espacio = request.json['idtipoespacio_espacio']
        if 'codespacio_espacio' in request.json:
            espacio.codespacio_espacio = request.json['codespacio_espacio']
        if 'nomespacio' in request.json:
            espacio.nomespacio = request.json['nomespacio']

        db.session.commit()
        return espacio_schema.dump(espacio)

    def delete(self, espacio_id):
        espacio = Espacio.query.get_or_404(espacio_id)
        db.session.delete(espacio)
        db.session.commit()
        return '', 204
