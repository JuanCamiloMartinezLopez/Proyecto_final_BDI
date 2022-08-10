from . import db,ma

class Rol(db.Model):
    __tablename__ = 'rol'

    idrol = db.Column(db.String(1), primary_key=True)
    descrol = db.Column(db.String(20), nullable=False)

class RolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Rol