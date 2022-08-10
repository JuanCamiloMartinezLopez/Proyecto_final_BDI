from . import db,ma

class Empleado(db.Model):
    __tablename__ = 'empleado'

    codempleado = db.Column(db.String(4), primary_key=True)
    nomempleado = db.Column(db.String(20), nullable=False)
    apellempleado = db.Column(db.String(20), nullable=False)
    fecharegistro = db.Column(db.Date, nullable=False)
    correoud = db.Column(db.String(30), nullable=False)

class EmpleadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Empleado
