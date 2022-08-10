from models import db
from models.asistirresponsableModel import Asistirresponsable,AsistirresponsableSchema
from flask import request
from flask_restful import Resource

asistirresponsable_schema = AsistirresponsableSchema()
asistirresponsables_schema = AsistirresponsableSchema(many=True)

class AsistirresponsablesResource(Resource):
    def get(self):
        asistirresponsables=Asistirresponsable.query.all()
        return asistirresponsables_schema.dump(asistirresponsables)

    def post(self):
        new_asistirresponsable = Asistirresponsable(
            consecprogra_responsable=request.json['consecprogra_responsable'],
            consecres_asistirresponsable=request.json['consecres_asistirresponsable'],
            consecasisres=request.json['consecasisres'],
            fechaasisres=request.json['fechaasisres'],
            horaasisres=request.json['horaasisres']
        )
        db.session.add(new_asistirresponsable)
        db.session.commit()
        return asistirresponsable_schema.dump(new_asistirresponsable)


class AsistirresponsableResource(Resource):
    def get(self, asistirresponsable_id):
        asistirresponsable = Asistirresponsable.query.get_or_404(asistirresponsable_id)
        return asistirresponsable_schema.dump(asistirresponsable)

    def patch(self, asistirresponsable_id):
        asistirresponsable = Asistirresponsable.query.get_or_404(asistirresponsable_id)

        if 'consecprogra_responsable' in request.json:
            asistirresponsable.consecprogra_responsable = request.json['consecprogra_responsable']
        if 'consecres_asistirresponsable' in request.json:
            asistirresponsable.consecres_asistirresponsable = request.json['consecres_asistirresponsable']
        if 'consecasisres' in request.json:
            asistirresponsable.consecasisres = request.json['consecasisres']
        if 'fechaasisres' in request.json:
            asistirresponsable.fechaasisres = request.json['fechaasisres']
        if 'horaasisres' in request.json:
            asistirresponsable.horaasisres = request.json['horaasisres']

        db.session.commit()
        return asistirresponsable_schema.dump(asistirresponsable)

    def delete(self, asistirresponsable_id):
        asistirresponsable = Asistirresponsable.query.get_or_404(asistirresponsable_id)
        db.session.delete(asistirresponsable)
        db.session.commit()
        return '', 204

