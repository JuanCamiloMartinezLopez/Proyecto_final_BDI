from . import db,ma

class Hora(db.Model):
    __tablename__ = 'hora'

    idhora = db.Column(db.String(5), primary_key=True)

class HoraSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Hora
        