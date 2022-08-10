from models import db
from models.rolModel import Rol,RolSchema
from flask import request
from flask_restful import Resource

rols_schema=RolSchema(many=True)
rol_schema=RolSchema()

class RolsResource(Resource):
    def get(self):
        rols=Rol.query.all()
        return rols_schema.dump(rols)

    def post(self):
        new_rol = Rol(
            idrol=request.json['idrol'],
            descrol=request.json['descrol'],
        )
        db.session.add(new_rol)
        db.session.commit()
        return rol_schema.dump(new_rol)


class RolResource(Resource):
    def get(self, rol_id):
        rol = Rol.query.get_or_404(rol_id)
        return rol_schema.dump(rol)

    def patch(self, rol_id):
        rol = Rol.query.get_or_404(rol_id)

        if 'idrol' in request.json:
            rol.idrol = request.json['idrol']
        if 'descrol' in request.json:
            rol.descrol = request.json['descrol']

        db.session.commit()
        return rol_schema.dump(rol)

    def delete(self, rol_id):
        rol = Rol.query.get_or_404(rol_id)
        db.session.delete(rol)
        db.session.commit()
        return '', 204
