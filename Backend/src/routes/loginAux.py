from models import db
from models.empleadocargoModel import EmpleadoCargo,EmpleadoCargoSchema
from models.empleadoModel import Empleado
from flask import request
from flask_restful import Resource
from datetime import date ,datetime

equipo_schema=EmpleadoCargoSchema()

class LoginAuxResource(Resource):
    def get(self,code_emp):
        auxiliar=EmpleadoCargo.query.filter_by(codempleado_empleadocargo=code_emp,idcargo_empleadocargo="1",fechafincar=None).first()
        if auxiliar is None:
            return {"login":False}, 404
        print(equipo_schema.dump(auxiliar))
        return {"info_empleado":equipo_schema.dump(auxiliar),"fecha":date.today().strftime("%d-%m-%Y"), "hora":datetime.now().strftime('%H:%M'),"login":True}

