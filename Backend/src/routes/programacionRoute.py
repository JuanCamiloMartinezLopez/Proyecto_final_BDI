from models import db
from models.programacionModel import Programacion,ProgramacionSchema
from flask import request
from flask_restful import Resource

programacions_schema=ProgramacionSchema(many=True)
programacion_schema=ProgramacionSchema()

class ProgramacionsResource(Resource):
    def get(self):
        programacions=Programacion.query.all()
        return programacions_schema.dump(programacions)

    def post(self):
        new_programacion = Programacion(
            consecprogra=request.json['consecprogra'],
            codespacio_programacion=request.json['codespacio_programacion'],
            iddeporte_programacion=request.json['iddeporte_programacion'],
            idperiodo_programacion=request.json['idperiodo_programacion'],
            idactividad_programacion=request.json['idactividad_programacion'],
            idhorainicio_programacion=request.json['idhorainicio_programacion'],
            idhorafin_programacion=request.json['idhorafin_programacion'],
            iddia_programacion=request.json['iddia_programacion'],
            cupo=request.json['cupo'],
            noinscrito=request.json['noinscrito'],
        )
        db.session.add(new_programacion)
        db.session.commit()
        return programacion_schema.dump(new_programacion)


class ProgramacionResource(Resource):
    def get(self, programacion_id):
        programacion = Programacion.query.get_or_404(programacion_id)
        return programacion_schema.dump(programacion)

    def patch(self, programacion_id):
        programacion = Programacion.query.get_or_404(programacion_id)

        if 'consecprogra' in request.json:
            programacion.consecprogra = request.json['consecprogra']
        if 'codespacio_programacion' in request.json:
            programacion.codespacio_programacion = request.json['codespacio_programacion']
        if 'iddeporte_programacion' in request.json:
            programacion.iddeporte_programacion = request.json['iddeporte_programacion']
        if 'idperiodo_programacion' in request.json:
            programacion.idperiodo_programacion = request.json['idperiodo_programacion']
        if 'idactividad_programacion' in request.json:
            programacion.idactividad_programacion = request.json['idactividad_programacion']
        if 'idhorainicio_programacion' in request.json:
            programacion.idhorainicio_programacion = request.json['idhorainicio_programacion']
        if 'idhorafin_programacion' in request.json:
            programacion.idhorafin_programacion = request.json['idhorafin_programacion']
        if 'iddia_programacion' in request.json:
            programacion.iddia_programacion = request.json['iddia_programacion']
        if 'cupo' in request.json:
            programacion.cupo = request.json['cupo']
        if 'noinscrito' in request.json:
            programacion.noinscrito = request.json['noinscrito']

        db.session.commit()
        return programacion_schema.dump(programacion)

    def delete(self, programacion_id):
        programacion = Programacion.query.get_or_404(programacion_id)
        db.session.delete(programacion)
        db.session.commit()
        return '', 204
