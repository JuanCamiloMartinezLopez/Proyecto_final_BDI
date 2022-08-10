from . import db,ma

class Estado(db.Model):
    __tablename__ = 'estado'

    idestado = db.Column(db.String(2), primary_key=True)
    descestado = db.Column(db.String(20), nullable=False)

class EstadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Estado