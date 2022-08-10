from models import db
from models.inscritopraclibreModel import Inscritopraclibre,InscritopraclibreSchema
from flask import request
from flask_restful import Resource

inscritopraclibres_schema=InscritopraclibreSchema(many=True)
inscritopraclibre_schema=InscritopraclibreSchema()

class InscritopraclibresResource(Resource):
    def get(self):
        inscritopraclibres=Inscritopraclibre.query.all()
        return inscritopraclibres_schema.dump(inscritopraclibres)

    def post(self):
        new_inscritopraclibre = Inscritopraclibre(
            consecprogra_inscritopraclibre=request.json['consecprogra_inscritopraclibre'],
            consecpract=request.json['consecpract'],
            codempleado_inscritopraclibre=request.json['codempleado_inscritopraclibre'],
            codestu_inscritopraclibre=request.json['codestu_inscritopraclibre'],
        )
        db.session.add(new_inscritopraclibre)
        db.session.commit()
        return inscritopraclibre_schema.dump(new_inscritopraclibre)


class InscritopraclibreResource(Resource):
    def get(self, inscritopraclibre_id):
        inscritopraclibre = Inscritopraclibre.query.get_or_404(inscritopraclibre_id)
        return inscritopraclibre_schema.dump(inscritopraclibre)

    def patch(self, inscritopraclibre_id):
        inscritopraclibre = Inscritopraclibre.query.get_or_404(inscritopraclibre_id)

        if 'consecprogra_inscritopraclibre' in request.json:
            inscritopraclibre.consecprogra_inscritopraclibre = request.json['consecprogra_inscritopraclibre']
        if 'consecpract' in request.json:
            inscritopraclibre.consecpract = request.json['consecpract']
        if 'codempleado_inscritopraclibre' in request.json:
            inscritopraclibre.codempleado_inscritopraclibre = request.json['codempleado_inscritopraclibre']
        if 'codestu_inscritopraclibre' in request.json:
            inscritopraclibre.codestu_inscritopraclibre = request.json['codestu_inscritopraclibre']

        db.session.commit()
        return inscritopraclibre_schema.dump(inscritopraclibre)

    def delete(self, inscritopraclibre_id):
        inscritopraclibre = Inscritopraclibre.query.get_or_404(inscritopraclibre_id)
        db.session.delete(inscritopraclibre)
        db.session.commit()
        return '', 204
