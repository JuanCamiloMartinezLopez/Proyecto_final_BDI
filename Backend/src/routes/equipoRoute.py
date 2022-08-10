from models import db
from models.equipoModel import Equipo,EquipoSchema
from flask import request
from flask_restful import Resource

equipos_schema=EquipoSchema(many=True)
equipo_schema=EquipoSchema()

class EquiposResource(Resource):
    def get(self):
        equipos=Equipo.query.all()
        return equipos_schema.dump(equipos)

    def post(self):
        new_equipo = Equipo(
            conseequipo=request.json['conseequipo'],
            iddeporte_equipo=request.json['iddeporte_equipo'],
            codempleado_equipo=request.json['codempleado_equipo'],
            fecharesol=request.json['fecharesol'],
        )
        db.session.add(new_equipo)
        db.session.commit()
        return equipo_schema.dump(new_equipo)


class EquipoResource(Resource):
    def get(self, equipo_id):
        equipo = Equipo.query.get_or_404(equipo_id)
        return equipo_schema.dump(equipo)

    def patch(self, equipo_id):
        equipo = Equipo.query.get_or_404(equipo_id)

        if 'conseequipo' in request.json:
            equipo.conseequipo = request.json['conseequipo']
        if 'iddeporte_equipo' in request.json:
            equipo.iddeporte_equipo = request.json['iddeporte_equipo']
        if 'codempleado_equipo' in request.json:
            equipo.codempleado_equipo = request.json['codempleado_equipo']
        if 'fecharesol' in request.json:
            equipo.fecharesol = request.json['fecharesol']

        db.session.commit()
        return equipo_schema.dump(equipo)

    def delete(self, equipo_id):
        equipo = Equipo.query.get_or_404(equipo_id)
        db.session.delete(equipo)
        db.session.commit()
        return '', 204
