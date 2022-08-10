from . import db,ma

class Actividad(db.Model):
    __tablename__ = 'actividad'

    idactividad = db.Column(db.String(2), primary_key=True)
    descactividad = db.Column(db.String(30), nullable=False)

class ActividadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Actividad