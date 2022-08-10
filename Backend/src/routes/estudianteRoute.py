from models import db
from models.estudianteModel import Estudiante,EstudianteSchema
from flask import request
from flask_restful import Resource

estudiantes_schema=EstudianteSchema(many=True)
estudiante_schema=EstudianteSchema()

class EstudiantesResource(Resource):
    def get(self):
        estudiantes=Estudiante.query.all()
        return estudiantes_schema.dump(estudiantes)

    def post(self):
        new_estudiante = Estudiante(
            codestu=request.json['codestu'],
            codespacio_estudiante=request.json['codespacio_estudiante'],
            nomestu=request.json['nomestu'],
            apelestu=request.json['apelestu'],
            fecharegestu=request.json['fecharegestu'],
            correoudestu=request.json['correoudestu'],
            fechanacestu=request.json['fechanacestu'],
        )
        db.session.add(new_estudiante)
        db.session.commit()
        return estudiante_schema.dump(new_estudiante)


class EstudianteResource(Resource):
    def get(self, estudiante_id):
        estudiante = Estudiante.query.get_or_404(estudiante_id)
        return estudiante_schema.dump(estudiante)

    def patch(self, estudiante_id):
        estudiante = Estudiante.query.get_or_404(estudiante_id)

        if 'codestu' in request.json:
            estudiante.codestu = request.json['codestu']
        if 'codespacio_estudiante' in request.json:
            estudiante.codespacio_estudiante = request.json['codespacio_estudiante']
        if 'nomestu' in request.json:
            estudiante.nomestu = request.json['nomestu']
        if 'apelestu' in request.json:
            estudiante.apelestu = request.json['apelestu']
        if 'fecharegestu' in request.json:
            estudiante.fecharegestu = request.json['fecharegestu']
        if 'correoudestu' in request.json:
            estudiante.correoudestu = request.json['correoudestu']
        if 'fechanacestu' in request.json:
            estudiante.fechanacestu = request.json['fechanacestu']

        db.session.commit()
        return estudiante_schema.dump(estudiante)

    def delete(self, estudiante_id):
        estudiante = Estudiante.query.get_or_404(estudiante_id)
        db.session.delete(estudiante)
        db.session.commit()
        return '', 204
