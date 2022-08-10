from . import db,ma

class Cargo(db.Model):
    __tablename__ = 'cargo'

    idcargo = db.Column(db.String(2), primary_key=True)
    descargo = db.Column(db.String(30), nullable=False)

class CargoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Cargo