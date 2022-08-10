from . import db,ma
from .programacionModel import Programacion
from .miembroequipoModel import Miembroequipo

class Asismiembroequipo(db.Model):
    __tablename__ = 'asismiembroequipo'
    __table_args__ = (
        db.ForeignKeyConstraint(['conseequipo_miemeq_asismiemeq', 'itemmiembro_asismiembroequipo'], ['miembroequipo.conseequipo_miembroequipo', 'miembroequipo.itemmiembro'], ondelete='RESTRICT', onupdate='RESTRICT'),
        db.Index('miembroequipo_asismiemeq_fk', 'conseequipo_miemeq_asismiemeq', 'itemmiembro_asismiembroequipo')
    )

    consecprogra_asismiembroequipo = db.Column(db.ForeignKey('programacion.consecprogra', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    conmiemequipo = db.Column(db.Integer, primary_key=True, nullable=False)
    conseequipo_miemeq_asismiemeq = db.Column(db.Integer, nullable=False)
    itemmiembro_asismiembroequipo = db.Column(db.Integer, nullable=False)

    programacion = db.relationship('Programacion', primaryjoin='Asismiembroequipo.consecprogra_asismiembroequipo == Programacion.consecprogra', backref='asismiembroequipoes')
    miembroequipo = db.relationship('Miembroequipo', primaryjoin='and_(Asismiembroequipo.conseequipo_miemeq_asismiemeq == Miembroequipo.conseequipo_miembroequipo, Asismiembroequipo.itemmiembro_asismiembroequipo == Miembroequipo.itemmiembro)', backref='asismiembroequipoes')

class AsismiembroequipoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Asismiembroequipo