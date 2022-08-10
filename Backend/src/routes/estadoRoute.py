from models import db
from models.estadoModel import Estado,EstadoSchema
from flask import request
from flask_restful import Resource

estados_schema=EstadoSchema(many=True)
estado_schema=EstadoSchema()

class EstadosResource(Resource):
    def get(self):
        estados=Estado.query.all()
        return estados_schema.dump(estados)

    def post(self):
        new_estado = Estado(
            idestado=request.json['idestado'],
            descestado=request.json['descestado'],
        )
        db.session.add(new_estado)
        db.session.commit()
        return estado_schema.dump(new_estado)


class EstadoResource(Resource):
    def get(self, estado_id):
        estado = Estado.query.get_or_404(estado_id)
        return estado_schema.dump(estado)

    def patch(self, estado_id):
        estado = Estado.query.get_or_404(estado_id)

        if 'idestado' in request.json:
            estado.idestado = request.json['idestado']
        if 'descestado' in request.json:
            estado.descestado = request.json['descestado']

        db.session.commit()
        return estado_schema.dump(estado)

    def delete(self, estado_id):
        estado = Estado.query.get_or_404(estado_id)
        db.session.delete(estado)
        db.session.commit()
        return '', 204
