from . import db,ma

class Periodo(db.Model):
    __tablename__ = 'periodo'

    idperiodo = db.Column(db.String(5), primary_key=True)

class PeriodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Periodo