from models import db
from models.deporteModel import Deporte,DeporteSchema
from flask import request
from flask_restful import Resource

deportes_schema=DeporteSchema(many=True)
deporte_schema=DeporteSchema()

class DeportesResource(Resource):
    def get(self):
        deportes=Deporte.query.all()
        return deportes_schema.dump(deportes)

    def post(self):
        new_deporte = Deporte(
            iddeporte=request.json['iddeporte'],
            nomdeporte=request.json['nomdeporte'],
        )
        db.session.add(new_deporte)
        db.session.commit()
        return deporte_schema.dump(new_deporte)


class DeporteResource(Resource):
    def get(self, deporte_id):
        deporte = Deporte.query.get_or_404(deporte_id)
        return deporte_schema.dump(deporte)

    def patch(self, deporte_id):
        deporte = Deporte.query.get_or_404(deporte_id)

        if 'iddeporte' in request.json:
            deporte.iddeporte = request.json['iddeporte']
        if 'nomdeporte' in request.json:
            deporte.nomdeporte = request.json['nomdeporte']

        db.session.commit()
        return deporte_schema.dump(deporte)

    def delete(self, deporte_id):
        deporte = Deporte.query.get_or_404(deporte_id)
        db.session.delete(deporte)
        db.session.commit()
        return '', 204

