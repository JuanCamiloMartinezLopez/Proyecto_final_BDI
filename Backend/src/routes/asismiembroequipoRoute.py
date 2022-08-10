from models import db
from models.asismiembroequipoModel import Asismiembroequipo,AsismiembroequipoSchema
from flask import request
from flask_restful import Resource

asismiembroequipo_schema = AsismiembroequipoSchema()
asismiembroequipos_schema = AsismiembroequipoSchema(many=True)

class AsismiembroequiposResource(Resource):
    def get(self):
        asismiembroequipos=Asismiembroequipo.query.all()
        return asismiembroequipos_schema.dump(asismiembroequipos)

    def post(self):
        new_asismiembroequipo = Asismiembroequipo(
            consecprogra_asismiembroequipo=request.json['consecprogra_asismiembroequipo'],
            conmiemequipo=request.json['conmiemequipo'],
            conseequipo_miemeq_asismiemeq=request.json['conseequipo_miemeq_asismiemeq'],
            itemmiembro_asismiembroequipo=request.json['itemmiembro_asismiembroequipo']
        )
        db.session.add(new_asismiembroequipo)
        db.session.commit()
        return asismiembroequipo_schema.dump(new_asismiembroequipo)


class AsismiembroequipoResource(Resource):
    def get(self, asismiembroequipo_id):
        asismiembroequipo = Asismiembroequipo.query.get_or_404(asismiembroequipo_id)
        return asismiembroequipo_schema.dump(asismiembroequipo)

    def patch(self, asismiembroequipo_id):
        asismiembroequipo = Asismiembroequipo.query.get_or_404(asismiembroequipo_id)

        if 'consecprogra_asismiembroequipo' in request.json:
            asismiembroequipo.consecprogra_asismiembroequipo = request.json['consecprogra_asismiembroequipo']
        if 'conmiemequipo' in request.json:
            asismiembroequipo.conmiemequipo = request.json['conmiemequipo']
        if 'conseequipo_miemeq_asismiemeq' in request.json:
            asismiembroequipo.conseequipo_miemeq_asismiemeq = request.json['conseequipo_miemeq_asismiemeq']
        if 'itemmiembro_asismiembroequipo' in request.json:
            asismiembroequipo.itemmiembro_asismiembroequipo = request.json['itemmiembro_asismiembroequipo']

        db.session.commit()
        return asismiembroequipo_schema.dump(asismiembroequipo)

    def delete(self, asismiembroequipo_id):
        asismiembroequipo = Asismiembroequipo.query.get_or_404(asismiembroequipo_id)
        db.session.delete(asismiembroequipo)
        db.session.commit()
        return '', 204

