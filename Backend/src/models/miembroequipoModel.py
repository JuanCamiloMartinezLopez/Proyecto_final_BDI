from . import db,ma
from .estudianteModel import Estudiante
from .equipoModel import Equipo
from .empleadoModel import Empleado

class Miembroequipo(db.Model):
    __tablename__ = 'miembroequipo'

    conseequipo_miembroequipo = db.Column(db.ForeignKey('equipo.conseequipo', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    itemmiembro = db.Column(db.Numeric(3, 0), primary_key=True, nullable=False)
    codestu_miembroequipo = db.Column(db.ForeignKey('estudiante.codestu', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    estudiante = db.relationship('Estudiante', primaryjoin='Miembroequipo.codestu_miembroequipo == Estudiante.codestu', backref='miembroequipoes')
    equipo = db.relationship('Equipo', primaryjoin='Miembroequipo.conseequipo_miembroequipo == Equipo.conseequipo', backref='miembroequipoes')

class MiembroequipoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Miembroequipo