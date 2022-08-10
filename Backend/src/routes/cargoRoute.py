from models import db
from models.cargoModel import Cargo,CargoSchema
from flask import request
from flask_restful import Resource

cargo_schema = CargoSchema()
cargos_schema = CargoSchema(many=True)

class CargosResource(Resource):
    def get(self):
        cargos=Cargo.query.all()
        return cargos_schema.dump(cargos)

    def post(self):
        new_cargo = Cargo(
            idcargo=request.json['idcargo'],
            descargo=request.json['descargo'],
        )
        db.session.add(new_cargo)
        db.session.commit()
        return cargo_schema.dump(new_cargo)


class CargoResource(Resource):
    def get(self, cargo_id):
        cargo = Cargo.query.get_or_404(cargo_id)
        return cargo_schema.dump(cargo)

    def patch(self, cargo_id):
        cargo = Cargo.query.get_or_404(cargo_id)

        if 'idcargo' in request.json:
            cargo.idcargo = request.json['idcargo']
        if 'descargo' in request.json:
            cargo.descargo = request.json['descargo']

        db.session.commit()
        return cargo_schema.dump(cargo)

    def delete(self, cargo_id):
        cargo = Cargo.query.get_or_404(cargo_id)
        db.session.delete(cargo)
        db.session.commit()
        return '', 204
