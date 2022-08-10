from models import db
from models.horaModel import Hora,HoraSchema
from flask import request
from flask_restful import Resource

horas_schema=HoraSchema(many=True)
hora_schema=HoraSchema()

class HorasResource(Resource):
    def get(self):
        horas=Hora.query.all()
        return horas_schema.dump(horas)

    def post(self):
        new_hora = Hora(
            idhora=request.json['idhora'],
        )
        db.session.add(new_hora)
        db.session.commit()
        return hora_schema.dump(new_hora)


class HoraResource(Resource):
    def get(self, hora_id):
        hora = Hora.query.get_or_404(hora_id)
        return hora_schema.dump(hora)

    def patch(self, hora_id):
        hora = Hora.query.get_or_404(hora_id)

        if 'idhora' in request.json:
            hora.idhora = request.json['idhora']

        db.session.commit()
        return hora_schema.dump(hora)

    def delete(self, hora_id):
        hora = Hora.query.get_or_404(hora_id)
        db.session.delete(hora)
        db.session.commit()
        return '', 204
