
from . import db,ma
from .espacioModel import EspacioSchema
from .empleadoModel import EmpleadoSchema
from .cargoModel import CargoSchema

class EmpleadoCargo(db.Model):
    __tablename__ = 'empleado_cargo'

    consec = db.Column(db.Integer, primary_key=True)
    codespacio_empleadocargo = db.Column(db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idcargo_empleadocargo = db.Column(db.ForeignKey('cargo.idcargo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    codempleado_empleadocargo = db.Column(db.ForeignKey('empleado.codempleado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    fechacargo = db.Column(db.Date, nullable=False)
    fechafincar = db.Column(db.Date)

    empleado = db.relationship('Empleado', primaryjoin='EmpleadoCargo.codempleado_empleadocargo == Empleado.codempleado', backref='empleado_cargoes')
    espacio = db.relationship('Espacio', primaryjoin='EmpleadoCargo.codespacio_empleadocargo == Espacio.codespacio', backref='empleado_cargoes')
    cargo = db.relationship('Cargo', primaryjoin='EmpleadoCargo.idcargo_empleadocargo == Cargo.idcargo', backref='empleado_cargoes')

class EmpleadoCargoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=EmpleadoCargo
        fields = ('consec', 'espacio', 'cargo','empleado','fechacargo','fechafincar')
    espacio=ma.Nested(EspacioSchema(only=('codespacio','nomespacio')))
    cargo=ma.Nested(CargoSchema)
    empleado=ma.Nested(EmpleadoSchema)