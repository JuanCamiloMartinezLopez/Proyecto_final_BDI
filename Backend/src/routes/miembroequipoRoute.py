from models import db
from models.miembroequipoModel import Miembroequipo,MiembroequipoSchema
from flask import request
from flask_restful import Resource

miembroequipos_schema=MiembroequipoSchema(many=True)
miembroequipo_schema=MiembroequipoSchema()

class MiembroequiposResource(Resource):
    def get(self):
        miembroequipos=Miembroequipo.query.all()
        return miembroequipos_schema.dump(miembroequipos)

    def post(self):
        new_miembroequipo = Miembroequipo(
            conseequipo_miembroequipo=request.json['conseequipo_miembroequipo'],
            itemmiembro=request.json['itemmiembro'],
            codestu_miembroequipo=request.json['codestu_miembroequipo'],
        )
        db.session.add(new_miembroequipo)
        db.session.commit()
        return miembroequipo_schema.dump(new_miembroequipo)


class MiembroequipoResource(Resource):
    def get(self, miembroequipo_id):
        miembroequipo = Miembroequipo.query.get_or_404(miembroequipo_id)
        return miembroequipo_schema.dump(miembroequipo)

    def patch(self, miembroequipo_id):
        miembroequipo = Miembroequipo.query.get_or_404(miembroequipo_id)

        if 'conseequipo_miembroequipo' in request.json:
            miembroequipo.conseequipo_miembroequipo = request.json['conseequipo_miembroequipo']
        if 'itemmiembro' in request.json:
            miembroequipo.itemmiembro = request.json['itemmiembro']
        if 'codestu_miembroequipo' in request.json:
            miembroequipo.codestu_miembroequipo = request.json['codestu_miembroequipo']

        db.session.commit()
        return miembroequipo_schema.dump(miembroequipo)

    def delete(self, miembroequipo_id):
        miembroequipo = Miembroequipo.query.get_or_404(miembroequipo_id)
        db.session.delete(miembroequipo)
        db.session.commit()
        return '', 204
