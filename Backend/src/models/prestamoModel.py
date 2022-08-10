from . import db,ma

class Prestamo(db.Model):
    __tablename__ = 'prestamo'
    __table_args__ = (
        db.ForeignKeyConstraint(['consecprogra_resp_prest', 'consecres_asisresp_prest', 'consecasisres_prestamo'], ['asistirresponsable.consecprogra_responsable', 'asistirresponsable.consecres_asistirresponsable', 'asistirresponsable.consecasisres'], ondelete='RESTRICT', onupdate='RESTRICT'),
        db.Index('asistirresponsable_prestamo_fk', 'consecprogra_resp_prest', 'consecres_asisresp_prest', 'consecasisres_prestamo')
    )

    consecprestamo = db.Column(db.Numeric(4, 0), primary_key=True)
    consecprogra_resp_prest = db.Column(db.Numeric(4, 0), nullable=False)
    consecres_asisresp_prest = db.Column(db.Numeric(4, 0), nullable=False)
    consecasisres_prestamo = db.Column(db.Numeric(4, 0), nullable=False)
    consecelemento_prestamo = db.Column(db.ForeignKey('elemendeportivo.consecelemento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    elemendeportivo = db.relationship('Elemendeportivo', primaryjoin='Prestamo.consecelemento_prestamo == Elemendeportivo.consecelemento', backref='prestamoes')
    asistirresponsable = db.relationship('Asistirresponsable', primaryjoin='and_(Prestamo.consecprogra_resp_prest == Asistirresponsable.consecprogra_responsable, Prestamo.consecres_asisresp_prest == Asistirresponsable.consecres_asistirresponsable, Prestamo.consecasisres_prestamo == Asistirresponsable.consecasisres)', backref='prestamoes')

class PrestamoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Prestamo