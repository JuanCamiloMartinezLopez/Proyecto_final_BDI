from . import db,ma
from .rolModel import Rol

class Responsable(db.Model):
    __tablename__ = 'responsable'

    consecprogra_responsable = db.Column(db.ForeignKey('programacion.consecprogra', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    consecres = db.Column(db.Numeric(4, 0), primary_key=True, nullable=False)
    codempleado_responsable = db.Column(db.ForeignKey('empleado.codempleado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    codestu_responsable = db.Column(db.ForeignKey('estudiante.codestu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    idrol_responsable = db.Column(db.ForeignKey('rol.idrol', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    fechaini = db.Column(db.Date, nullable=False)
    fechafin = db.Column(db.Date, nullable=False)

    empleado = db.relationship('Empleado', primaryjoin='Responsable.codempleado_responsable == Empleado.codempleado', backref='responsables')
    estudiante = db.relationship('Estudiante', primaryjoin='Responsable.codestu_responsable == Estudiante.codestu', backref='responsables')
    programacion = db.relationship('Programacion', primaryjoin='Responsable.consecprogra_responsable == Programacion.consecprogra', backref='responsables')
    rol = db.relationship('Rol', primaryjoin='Responsable.idrol_responsable == Rol.idrol', backref='responsables')

class ResponsableSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Responsable