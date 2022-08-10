from . import db,ma
from .espacioModel import Espacio
from .diaModel import Dia
from .horaModel import Hora
from .periodoModel import Periodo

class Programacion(db.Model):
    __tablename__ = 'programacion'

    consecprogra = db.Column(db.Numeric(4, 0), primary_key=True)
    codespacio_programacion = db.Column(db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    iddeporte_programacion = db.Column(db.ForeignKey('deporte.iddeporte', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idperiodo_programacion = db.Column(db.ForeignKey('periodo.idperiodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idactividad_programacion = db.Column(db.ForeignKey('actividad.idactividad', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idhorainicio_programacion = db.Column(db.ForeignKey('hora.idhora', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idhorafin_programacion = db.Column(db.ForeignKey('hora.idhora', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    iddia_programacion = db.Column(db.ForeignKey('dia.iddia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cupo = db.Column(db.Numeric(3, 0), nullable=False)
    noinscrito = db.Column(db.Numeric(3, 0), nullable=False)

    espacio = db.relationship('Espacio', primaryjoin='Programacion.codespacio_programacion == Espacio.codespacio', backref='programacions')
    actividad = db.relationship('Actividad', primaryjoin='Programacion.idactividad_programacion == Actividad.idactividad', backref='programacions')
    deporte = db.relationship('Deporte', primaryjoin='Programacion.iddeporte_programacion == Deporte.iddeporte', backref='programacions')
    dia = db.relationship('Dia', primaryjoin='Programacion.iddia_programacion == Dia.iddia', backref='programacions')
    hora = db.relationship('Hora', primaryjoin='Programacion.idhorafin_programacion == Hora.idhora', backref='hora_programacions')
    hora1 = db.relationship('Hora', primaryjoin='Programacion.idhorainicio_programacion == Hora.idhora', backref='hora_programacions_0')
    periodo = db.relationship('Periodo', primaryjoin='Programacion.idperiodo_programacion == Periodo.idperiodo', backref='programacions')

class ProgramacionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Programacion
        