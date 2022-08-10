from . import db,ma

class Marca(db.Model):
    __tablename__ = 'marca'

    idmarca = db.Column(db.String(3), primary_key=True)
    nommarca = db.Column(db.String(20), nullable=False)

class MarcaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Marca