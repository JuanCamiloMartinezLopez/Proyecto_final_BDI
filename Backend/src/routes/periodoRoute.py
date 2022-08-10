from models import db
from models.periodoModel import Periodo,PeriodoSchema
from flask import request
from flask_restful import Resource

periodos_schema=PeriodoSchema(many=True)
periodo_schema=PeriodoSchema()

class PeriodosResource(Resource):
    def get(self):
        periodos=Periodo.query.all()
        return periodos_schema.dump(periodos)

    def post(self):
        new_periodo = Periodo(
            idperiodo=request.json['idperiodo'],
        )
        db.session.add(new_periodo)
        db.session.commit()
        return periodo_schema.dump(new_periodo)


class PeriodoResource(Resource):
    def get(self, periodo_id):
        periodo = Periodo.query.get_or_404(periodo_id)
        return periodo_schema.dump(periodo)

    def patch(self, periodo_id):
        periodo = Periodo.query.get_or_404(periodo_id)

        if 'idperiodo' in request.json:
            periodo.idperiodo = request.json['idperiodo']

        db.session.commit()
        return periodo_schema.dump(periodo)

    def delete(self, periodo_id):
        periodo = Periodo.query.get_or_404(periodo_id)
        db.session.delete(periodo)
        db.session.commit()
        return '', 204
