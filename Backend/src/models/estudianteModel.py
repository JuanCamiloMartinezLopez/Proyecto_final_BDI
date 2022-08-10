from . import db,ma

class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    codestu = db.Column(db.String(12), primary_key=True)
    codespacio_estudiante = db.Column(db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nomestu = db.Column(db.String(30), nullable=False)
    apelestu = db.Column(db.String(30), nullable=False)
    fecharegestu = db.Column(db.Date, nullable=False)
    correoudestu = db.Column(db.String(30), nullable=False)
    fechanacestu = db.Column(db.Date, nullable=False)

    espacio = db.relationship('Espacio', primaryjoin='Estudiante.codespacio_estudiante == Espacio.codespacio', backref='estudiantes')

class EstudianteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Estudiante