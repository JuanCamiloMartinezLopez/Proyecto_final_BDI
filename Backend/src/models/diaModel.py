from http.client import ImproperConnectionState
from . import db,ma

class Dia(db.Model):
    __tablename__ = 'dia'

    iddia = db.Column(db.String(2), primary_key=True)
    nomdia = db.Column(db.String(10), nullable=False)

class DiaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Dia