from models import db
from models.empleadocargoModel import EmpleadoCargo,EmpleadoCargoSchema
from flask import request
from flask_restful import Resource

empleadocargos_schema=EmpleadoCargoSchema(many=True)
empleadocargo_schema=EmpleadoCargoSchema()

class EmpleadoCargosResource(Resource):
    def get(self):
        empleadocargos=EmpleadoCargo.query.all()
        return empleadocargos_schema.dump(empleadocargos)

    def post(self):
        new_empleadocargo = EmpleadoCargo(
            consec=request.json['consec'],
            codespacio_empleadocargo=request.json['codespacio_empleadocargo'],
            idcargo_empleadocargo=request.json['idcargo_empleadocargo'],
            codempleado_empleadocargo=request.json['codempleado_empleadocargo'],
            fechacargo=request.json['fechacargo'],
            fechafincar=request.json['fechafincar'],
        )
        db.session.add(new_empleadocargo)
        db.session.commit()
        return empleadocargo_schema.dump(new_empleadocargo)


class EmpleadoCargoResource(Resource):
    def get(self, empleadocargo_id):
        empleadocargo = EmpleadoCargo.query.get_or_404(empleadocargo_id)
        return empleadocargo_schema.dump(empleadocargo)

    def patch(self, empleadocargo_id):
        empleadocargo = EmpleadoCargo.query.get_or_404(empleadocargo_id)

        if 'consec' in request.json:
            empleadocargo.consec = request.json['consec']
        if 'codespacio_empleadocargo' in request.json:
            empleadocargo.codespacio_empleadocargo = request.json['codespacio_empleadocargo']
        if 'idcargo_empleadocargo' in request.json:
            empleadocargo.idcargo_empleadocargo = request.json['idcargo_empleadocargo']
        if 'codempleado_empleadocargo' in request.json:
            empleadocargo.codempleado_empleadocargo = request.json['codempleado_empleadocargo']
        if 'fechacargo' in request.json:
            empleadocargo.fechacargo = request.json['fechacargo']
        if 'fechafincar' in request.json:
            empleadocargo.fechafincar = request.json['fechafincar']

        db.session.commit()
        return empleadocargo_schema.dump(empleadocargo)

    def delete(self, empleadocargo_id):
        empleadocargo = EmpleadoCargo.query.get_or_404(empleadocargo_id)
        db.session.delete(empleadocargo)
        db.session.commit()
        return '', 204