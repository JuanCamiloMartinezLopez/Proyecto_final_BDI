from models import db
from models.elemendeportivoModel import Elemendeportivo,ElemendeportivoSchema
from flask import request
from flask_restful import Resource

elemendeportivos_schema=ElemendeportivoSchema(many=True)
elemendeportivo_schema=ElemendeportivoSchema()

class ElemendeportivosResource(Resource):
    def get(self):
        elemendeportivos=Elemendeportivo.query.all()
        return elemendeportivos_schema.dump(elemendeportivos)

    def post(self):
        new_elemendeportivo = Elemendeportivo(
            consecelemento=request.json['consecelemento'],
            codespacio_elemendeportivo=request.json['codespacio_elemendeportivo'],
            idtipoelemento_elemendeportivo=request.json['idtipoelemento_elemendeportivo'],
            idestado_elemendeportivo=request.json['idestado_elemendeportivo'],
            idmarca_elemendeportivo=request.json['idmarca_elemendeportivo'],
            fecharegistro=request.json['fecharegistro'],
        )
        db.session.add(new_elemendeportivo)
        db.session.commit()
        return elemendeportivo_schema.dump(new_elemendeportivo)


class ElemendeportivoResource(Resource):
    def get(self, elemendeportivo_id):
        elemendeportivo = Elemendeportivo.query.get_or_404(elemendeportivo_id)
        return elemendeportivo_schema.dump(elemendeportivo)

    def patch(self, elemendeportivo_id):
        elemendeportivo = Elemendeportivo.query.get_or_404(elemendeportivo_id)

        if 'consecelemento' in request.json:
            elemendeportivo.consecelemento = request.json['consecelemento']
        if 'codespacio_elemendeportivo' in request.json:
            elemendeportivo.codespacio_elemendeportivo = request.json['codespacio_elemendeportivo']
        if 'idtipoelemento_elemendeportivo' in request.json:
            elemendeportivo.idtipoelemento_elemendeportivo = request.json['idtipoelemento_elemendeportivo']
        if 'idestado_elemendeportivo' in request.json:
            elemendeportivo.idestado_elemendeportivo = request.json['idestado_elemendeportivo']
        if 'idmarca_elemendeportivo' in request.json:
            elemendeportivo.idmarca_elemendeportivo = request.json['idmarca_elemendeportivo']
        if 'fecharegistro' in request.json:
            elemendeportivo.fecharegistro = request.json['fecharegistro']

        db.session.commit()
        return elemendeportivo_schema.dump(elemendeportivo)

    def delete(self, elemendeportivo_id):
        elemendeportivo = Elemendeportivo.query.get_or_404(elemendeportivo_id)
        db.session.delete(elemendeportivo)
        db.session.commit()
        return '', 204