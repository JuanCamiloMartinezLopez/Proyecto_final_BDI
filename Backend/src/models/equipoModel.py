from . import db, ma
from .empleadoModel import Empleado

class Equipo(db.Model):
    __tablename__ = 'equipo'

    conseequipo = db.Column(db.Integer, primary_key=True)
    iddeporte_equipo = db.Column(db.ForeignKey('deporte.iddeporte', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    codempleado_equipo = db.Column(db.ForeignKey('empleado.codempleado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    fecharesol = db.Column(db.Date, nullable=False)

    empleado = db.relationship('Empleado', primaryjoin='Equipo.codempleado_equipo == Empleado.codempleado', backref='equipoes')
    deporte = db.relationship('Deporte', primaryjoin='Equipo.iddeporte_equipo == Deporte.iddeporte', backref='equipoes')

class EquipoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Equipo