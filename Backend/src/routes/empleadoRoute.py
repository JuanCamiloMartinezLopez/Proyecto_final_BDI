from models import db
from models.empleadoModel import Empleado,EmpleadoSchema
from flask import request
from flask_restful import Resource

empleados_schema=EmpleadoSchema(many=True)
empleado_schema=EmpleadoSchema()

class EmpleadosResource(Resource):
    def get(self):
        empleados=Empleado.query.all()
        return empleados_schema.dump(empleados)

    def post(self):
        new_empleado = Empleado(
            codempleado=request.json['codempleado'],
            nomempleado=request.json['nomempleado'],
            apellempleado=request.json['apellempleado'],
            fecharegistro=request.json['fecharegistro'],
            correoud=request.json['correoud'],
        )
        db.session.add(new_empleado)
        db.session.commit()
        return empleado_schema.dump(new_empleado)


class EmpleadoResource(Resource):
    def get(self, empleado_id):
        empleado = Empleado.query.get_or_404(empleado_id)
        return empleado_schema.dump(empleado)

    def patch(self, empleado_id):
        empleado = Empleado.query.get_or_404(empleado_id)

        if 'codempleado' in request.json:
            empleado.codempleado = request.json['codempleado']
        if 'nomempleado' in request.json:
            empleado.nomempleado = request.json['nomempleado']
        if 'apellempleado' in request.json:
            empleado.apellempleado = request.json['apellempleado']
        if 'fecharegistro' in request.json:
            empleado.fecharegistro = request.json['fecharegistro']
        if 'correoud' in request.json:
            empleado.correoud = request.json['correoud']

        db.session.commit()
        return empleado_schema.dump(empleado)

    def delete(self, empleado_id):
        empleado = Empleado.query.get_or_404(empleado_id)
        db.session.delete(empleado)
        db.session.commit()
        return '', 204
