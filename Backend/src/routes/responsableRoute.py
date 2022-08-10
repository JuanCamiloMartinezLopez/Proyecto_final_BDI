from models import db
from models.responsableModel import Responsable,ResponsableSchema
from flask import request
from flask_restful import Resource

responsables_schema=ResponsableSchema(many=True)
responsable_schema=ResponsableSchema()

class ResponsablesResource(Resource):
    def get(self):
        responsables=Responsable.query.all()
        return responsables_schema.dump(responsables)

    def post(self):
        new_responsable = Responsable(
            consecprogra_responsable=request.json['consecprogra_responsable'],
            consecres=request.json['consecres'],
            codempleado_responsable=request.json['codempleado_responsable'],
            codestu_responsable=request.json['codestu_responsable'],
            idrol_responsable=request.json['idrol_responsable'],
            fechaini=request.json['fechaini'],
            fechafin=request.json['fechafin'],
        )
        db.session.add(new_responsable)
        db.session.commit()
        return responsable_schema.dump(new_responsable)


class ResponsableResource(Resource):
    def get(self, responsable_id):
        responsable = Responsable.query.get_or_404(responsable_id)
        return responsable_schema.dump(responsable)

    def patch(self, responsable_id):
        responsable = Responsable.query.get_or_404(responsable_id)

        if 'consecprogra_responsable' in request.json:
            responsable.consecprogra_responsable = request.json['consecprogra_responsable']
        if 'consecres' in request.json:
            responsable.consecres = request.json['consecres']
        if 'codempleado_responsable' in request.json:
            responsable.codempleado_responsable = request.json['codempleado_responsable']
        if 'codestu_responsable' in request.json:
            responsable.codestu_responsable = request.json['codestu_responsable']
        if 'idrol_responsable' in request.json:
            responsable.idrol_responsable = request.json['idrol_responsable']
        if 'fechaini' in request.json:
            responsable.fechaini = request.json['fechaini']
        if 'fechafin' in request.json:
            responsable.fechafin = request.json['fechafin']

        db.session.commit()
        return responsable_schema.dump(responsable)

    def delete(self, responsable_id):
        responsable = Responsable.query.get_or_404(responsable_id)
        db.session.delete(responsable)
        db.session.commit()
        return '', 204
