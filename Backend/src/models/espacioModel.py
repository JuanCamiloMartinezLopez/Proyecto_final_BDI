from . import db, ma
from .deporteModel import DeporteSchema
from .tipoespacioModel import Tipoespacio

t_espacio_deporte = db.Table(
    'espacio_deporte',
    db.Column('codespacio_espaciodeporte', db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True),
    db.Column('iddeporte_espaciodeporte', db.ForeignKey('deporte.iddeporte', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
)

class Espacio(db.Model):
    __tablename__ = 'espacio'

    codespacio = db.Column(db.String(2), primary_key=True)
    idtipoespacio_espacio = db.Column(db.ForeignKey('tipoespacio.idtipoespacio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    codespacio_espacio = db.Column(db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nomespacio = db.Column(db.String(30), nullable=False)

    parent = db.relationship('Espacio', remote_side=[codespacio], primaryjoin='Espacio.codespacio_espacio == Espacio.codespacio', backref='espacios')
    tipoespacio = db.relationship('Tipoespacio', primaryjoin='Espacio.idtipoespacio_espacio == Tipoespacio.idtipoespacio', backref='espacios')
    deporte = db.relationship('Deporte', secondary='espacio_deporte', backref='espacios')

class EspacioSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model=Espacio
        fields=("codespacio","nomespacio","deporte")
    deporte=ma.Nested(DeporteSchema,many=True)