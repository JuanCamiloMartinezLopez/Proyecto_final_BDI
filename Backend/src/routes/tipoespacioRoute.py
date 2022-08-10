from models import db
from models.tipoespacioModel import Tipoespacio,TipoespacioSchema
from flask import request
from flask_restful import Resource

tipoespacios_schema=TipoespacioSchema(many=True)
tipoespacio_schema=TipoespacioSchema()

class TipoespaciosResource(Resource):
    def get(self):
        tipoespacios=Tipoespacio.query.all()
        return tipoespacios_schema.dump(tipoespacios)

    def post(self):
        new_tipoespacio = Tipoespacio(
            idtipoespacio=request.json['idtipoespacio'],
            desctipoespacio=request.json['desctipoespacio'],
        )
        db.session.add(new_tipoespacio)
        db.session.commit()
        return tipoespacio_schema.dump(new_tipoespacio)


class TipoespacioResource(Resource):
    def get(self, tipoespacio_id):
        tipoespacio = Tipoespacio.query.get_or_404(tipoespacio_id)
        return tipoespacio_schema.dump(tipoespacio)

    def patch(self, tipoespacio_id):
        tipoespacio = Tipoespacio.query.get_or_404(tipoespacio_id)

        if 'idtipoespacio' in request.json:
            tipoespacio.idtipoespacio = request.json['idtipoespacio']
        if 'desctipoespacio' in request.json:
            tipoespacio.desctipoespacio = request.json['desctipoespacio']

        db.session.commit()
        return tipoespacio_schema.dump(tipoespacio)

    def delete(self, tipoespacio_id):
        tipoespacio = Tipoespacio.query.get_or_404(tipoespacio_id)
        db.session.delete(tipoespacio)
        db.session.commit()
        return '', 204
