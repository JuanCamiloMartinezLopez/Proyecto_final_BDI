from models import db
from models.actividadModel import Actividad,ActividadSchema
from flask import request
from flask_restful import Resource

actividad_schema = ActividadSchema()
actividades_schema = ActividadSchema(many=True)

class ActividadesResource(Resource):
    def get(self):
        actividades=Actividad.query.all()
        return actividades_schema.dump(actividades)

    def post(self):
        print(request.json['idactividad'])
        new_actividad = Actividad(
            idactividad=request.json['idactividad'],
            descactividad=request.json['descactividad']
        )
        db.session.add(new_actividad)
        db.session.commit()
        return actividad_schema.dump(new_actividad)


class ActividadResource(Resource):
    def get(self, actividad_id):
        actividad = Actividad.query.get_or_404(actividad_id)
        return actividad_schema.dump(actividad)

    def patch(self, actividad_id):
        actividad = Actividad.query.get_or_404(actividad_id)

        if 'idactividad' in request.json:
            actividad.idactividad = request.json['idactividad']
        if 'descactividad' in request.json:
            actividad.descactividad = request.json['descactividad']

        db.session.commit()
        return actividad_schema.dump(actividad)

    def delete(self, actividad_id):
        actividad = Actividad.query.get_or_404(actividad_id)
        db.session.delete(actividad)
        db.session.commit()
        return '', 204

