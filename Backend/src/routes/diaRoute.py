from models import db
from models.diaModel import Dia,DiaSchema
from flask import request
from flask_restful import Resource

dias_schema=DiaSchema(many=True)
dia_schema=DiaSchema()

class DiasResource(Resource):
    def get(self):
        dias=Dia.query.all()
        return dias_schema.dump(dias)

    def post(self):
        new_dia = Dia(
            iddia=request.json['iddia'],
            nomdia=request.json['nomdia'],
        )
        db.session.add(new_dia)
        db.session.commit()
        return dia_schema.dump(new_dia)


class DiaResource(Resource):
    def get(self, dia_id):
        dia = Dia.query.get_or_404(dia_id)
        return dia_schema.dump(dia)

    def patch(self, dia_id):
        dia = Dia.query.get_or_404(dia_id)

        if 'iddia' in request.json:
            dia.iddia = request.json['iddia']
        if 'nomdia' in request.json:
            dia.nomdia = request.json['nomdia']

        db.session.commit()
        return dia_schema.dump(dia)

    def delete(self, dia_id):
        dia = Dia.query.get_or_404(dia_id)
        db.session.delete(dia)
        db.session.commit()
        return '', 204
