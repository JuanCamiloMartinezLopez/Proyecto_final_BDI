from . import db,ma
from .responsableModel import Responsable

class Asistirresponsable(db.Model):
    __tablename__ = 'asistirresponsable'
    __table_args__ = (
        db.ForeignKeyConstraint(['consecprogra_responsable', 'consecres_asistirresponsable'], ['responsable.consecprogra_responsable', 'responsable.consecres'], ondelete='RESTRICT', onupdate='RESTRICT'),
        db.Index('responsable_asisresp_fk', 'consecprogra_responsable', 'consecres_asistirresponsable')
    )

    consecprogra_responsable = db.Column(db.Numeric(4, 0), primary_key=True, nullable=False)
    consecres_asistirresponsable = db.Column(db.Numeric(4, 0), primary_key=True, nullable=False)
    consecasisres = db.Column(db.Numeric(4, 0), primary_key=True, nullable=False)
    fechaasisres = db.Column(db.Date, nullable=False)
    horaasisres = db.Column(db.Date, nullable=False)

    responsable = db.relationship('Responsable', primaryjoin='and_(Asistirresponsable.consecprogra_responsable == Responsable.consecprogra_responsable, Asistirresponsable.consecres_asistirresponsable == Responsable.consecres)', backref='asistirresponsables')

class AsistirresponsableSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Asistirresponsable