from models import db
from models.prestamoModel import Prestamo,PrestamoSchema
from flask import request
from flask_restful import Resource

prestamos_schema=PrestamoSchema(many=True)
prestamo_schema=PrestamoSchema()

class PrestamosResource(Resource):
    def get(self):
        prestamos=Prestamo.query.all()
        return prestamos_schema.dump(prestamos)

    def post(self):
        new_prestamo = Prestamo(
            consecprestamo=request.json['consecprestamo'],
            consecprogra_resp_prest=request.json['consecprogra_resp_prest'],
            consecres_asisresp_prest=request.json['consecres_asisresp_prest'],
            consecasisres_prestamo=request.json['consecasisres_prestamo'],
            consecelemento_prestamo=request.json['consecelemento_prestamo'],
        )
        db.session.add(new_prestamo)
        db.session.commit()
        return prestamo_schema.dump(new_prestamo)


class PrestamoResource(Resource):
    def get(self, prestamo_id):
        prestamo = Prestamo.query.get_or_404(prestamo_id)
        return prestamo_schema.dump(prestamo)

    def patch(self, prestamo_id):
        prestamo = Prestamo.query.get_or_404(prestamo_id)

        if 'consecprestamo' in request.json:
            prestamo.consecprestamo = request.json['consecprestamo']
        if 'consecprogra_resp_prest' in request.json:
            prestamo.consecprogra_resp_prest = request.json['consecprogra_resp_prest']
        if 'consecres_asisresp_prest' in request.json:
            prestamo.consecres_asisresp_prest = request.json['consecres_asisresp_prest']
        if 'consecasisres_prestamo' in request.json:
            prestamo.consecasisres_prestamo = request.json['consecasisres_prestamo']
        if 'consecelemento_prestamo' in request.json:
            prestamo.consecelemento_prestamo = request.json['consecelemento_prestamo']

        db.session.commit()
        return prestamo_schema.dump(prestamo)

    def delete(self, prestamo_id):
        prestamo = Prestamo.query.get_or_404(prestamo_id)
        db.session.delete(prestamo)
        db.session.commit()
        return '', 204
