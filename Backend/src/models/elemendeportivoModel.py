from . import db,ma
from .estadoModel import Estado
from .marcaModel import Marca

class Elemendeportivo(db.Model):
    __tablename__ = 'elemendeportivo'

    consecelemento = db.Column(db.Numeric(5, 0), primary_key=True)
    codespacio_elemendeportivo = db.Column(db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idtipoelemento_elemendeportivo = db.Column(db.ForeignKey('tipoelemento.idtipoelemento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idestado_elemendeportivo = db.Column(db.ForeignKey('estado.idestado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idmarca_elemendeportivo = db.Column(db.ForeignKey('marca.idmarca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    fecharegistro = db.Column(db.Date, nullable=False)

    espacio = db.relationship('Espacio', primaryjoin='Elemendeportivo.codespacio_elemendeportivo == Espacio.codespacio', backref='elemendeportivoes')
    estado = db.relationship('Estado', primaryjoin='Elemendeportivo.idestado_elemendeportivo == Estado.idestado', backref='elemendeportivoes')
    marca = db.relationship('Marca', primaryjoin='Elemendeportivo.idmarca_elemendeportivo == Marca.idmarca', backref='elemendeportivoes')
    tipoelemento = db.relationship('Tipoelemento', primaryjoin='Elemendeportivo.idtipoelemento_elemendeportivo == Tipoelemento.idtipoelemento', backref='elemendeportivoes')

class ElemendeportivoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Elemendeportivo