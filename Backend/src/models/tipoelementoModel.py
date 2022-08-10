from . import db,ma

class Tipoelemento(db.Model):
    __tablename__ = 'tipoelemento'

    idtipoelemento = db.Column(db.String(2), primary_key=True)
    desctipoelemento = db.Column(db.String(40), nullable=False)

class TipoelementoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields=("idtipoelemento","desctipoelemento")