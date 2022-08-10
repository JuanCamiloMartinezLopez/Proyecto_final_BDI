from . import db,ma
from .tipoelementoModel import TipoelementoSchema

t_deporte_tipoelemento = db.Table(
    'deporte_tipoelemento',
    db.Column('idtipoelemento_deportipoele', db.ForeignKey('tipoelemento.idtipoelemento', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True),
    db.Column('iddeporte_deportetipoelemento', db.ForeignKey('deporte.iddeporte', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
)

class Deporte(db.Model):
    __tablename__ = 'deporte'

    iddeporte = db.Column(db.String(2), primary_key=True)
    nomdeporte = db.Column(db.String(20), nullable=False)

    tipoelemento = db.relationship('Tipoelemento', secondary='deporte_tipoelemento', backref='deportes')

class DeporteSchema(ma.SQLAlchemyAutoSchema):
    tipoelemento=ma.Nested(TipoelementoSchema,many=True)
    class Meta:
        model=Deporte