from . import db,ma

class Inscritopraclibre(db.Model):
    __tablename__ = 'inscritopraclibre'

    consecprogra_inscritopraclibre = db.Column(db.ForeignKey('programacion.consecprogra', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    consecpract = db.Column(db.Integer, primary_key=True, nullable=False)
    codempleado_inscritopraclibre = db.Column(db.ForeignKey('empleado.codempleado', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    codestu_inscritopraclibre = db.Column(db.ForeignKey('estudiante.codestu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    empleado = db.relationship('Empleado', primaryjoin='Inscritopraclibre.codempleado_inscritopraclibre == Empleado.codempleado', backref='inscritopraclibres')
    estudiante = db.relationship('Estudiante', primaryjoin='Inscritopraclibre.codestu_inscritopraclibre == Estudiante.codestu', backref='inscritopraclibres')
    programacion = db.relationship('Programacion', primaryjoin='Inscritopraclibre.consecprogra_inscritopraclibre == Programacion.consecprogra', backref='inscritopraclibres')

class InscritopraclibreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Inscritopraclibre