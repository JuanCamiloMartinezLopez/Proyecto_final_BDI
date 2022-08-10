from . import db,ma

class Tipoespacio(db.Model):
    __tablename__ = 'tipoespacio'

    idtipoespacio = db.Column(db.String(2), primary_key=True)
    desctipoespacio = db.Column(db.String(30), nullable=False)

class TipoespacioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Tipoespacio
        