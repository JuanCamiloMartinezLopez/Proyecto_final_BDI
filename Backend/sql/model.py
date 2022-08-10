# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Actividad(db.Model):
    __tablename__ = 'actividad'

    idactividad = db.Column(db.String(2), primary_key=True)
    descactividad = db.Column(db.String(30), nullable=False)



class Asismiembroequipo(db.Model):
    __tablename__ = 'asismiembroequipo'
    __table_args__ = (
        db.ForeignKeyConstraint(['conseequipo_miemeq_asismiemeq', 'itemmiembro_asismiembroequipo'], ['miembroequipo.conseequipo_miembroequipo', 'miembroequipo.itemmiembro'], ondelete='RESTRICT', onupdate='RESTRICT'),
        db.Index('miembroequipo_asismiemeq_fk', 'conseequipo_miemeq_asismiemeq', 'itemmiembro_asismiembroequipo')
    )

    consecprogra_asismiembroequipo = db.Column(db.ForeignKey('programacion.consecprogra', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    conmiemequipo = db.Column(db.Integer, primary_key=True, nullable=False)
    conseequipo_miemeq_asismiemeq = db.Column(db.Integer, nullable=False)
    itemmiembro_asismiembroequipo = db.Column(db.Integer, nullable=False)

    programacion = db.relationship('Programacion', primaryjoin='Asismiembroequipo.consecprogra_asismiembroequipo == Programacion.consecprogra', backref='asismiembroequipoes')
    miembroequipo = db.relationship('Miembroequipo', primaryjoin='and_(Asismiembroequipo.conseequipo_miemeq_asismiemeq == Miembroequipo.conseequipo_miembroequipo, Asismiembroequipo.itemmiembro_asismiembroequipo == Miembroequipo.itemmiembro)', backref='asismiembroequipoes')



class Asistirresponsable(db.Model):
    __tablename__ = 'asistirresponsable'
    __table_args__ = (
        db.ForeignKeyConstraint(['consecprogra_responsable', 'consecres_asistirresponsable'], ['responsable.consecprogra_responsable', 'responsable.consecres'], ondelete='RESTRICT', onupdate='RESTRICT'),
        db.Index('responsable_asisresp_fk', 'consecprogra_responsable', 'consecres_asistirresponsable')
    )

    consecprogra_responsable = db.Column(db.Integer, primary_key=True, nullable=False)
    consecres_asistirresponsable = db.Column(db.Integer, primary_key=True, nullable=False)
    consecasisres = db.Column(db.Integer, primary_key=True, nullable=False)
    fechaasisres = db.Column(db.Date, nullable=False)
    horaasisres = db.Column(db.Date, nullable=False)

    responsable = db.relationship('Responsable', primaryjoin='and_(Asistirresponsable.consecprogra_responsable == Responsable.consecprogra_responsable, Asistirresponsable.consecres_asistirresponsable == Responsable.consecres)', backref='asistirresponsables')



class Cargo(db.Model):
    __tablename__ = 'cargo'

    idcargo = db.Column(db.String(2), primary_key=True)
    descargo = db.Column(db.String(30), nullable=False)



class Deporte(db.Model):
    __tablename__ = 'deporte'

    iddeporte = db.Column(db.String(2), primary_key=True)
    nomdeporte = db.Column(db.String(20), nullable=False)

    tipoelemento = db.relationship('Tipoelemento', secondary='deporte_tipoelemento', backref='deportes')



t_deporte_tipoelemento = db.Table(
    'deporte_tipoelemento',
    db.Column('idtipoelemento_deportipoele', db.ForeignKey('tipoelemento.idtipoelemento', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True),
    db.Column('iddeporte_deportetipoelemento', db.ForeignKey('deporte.iddeporte', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
)



class Dia(db.Model):
    __tablename__ = 'dia'

    iddia = db.Column(db.String(2), primary_key=True)
    nomdia = db.Column(db.String(10), nullable=False)



class Elemendeportivo(db.Model):
    __tablename__ = 'elemendeportivo'

    consecelemento = db.Column(db.Integer, primary_key=True)
    codespacio_elemendeportivo = db.Column(db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idtipoelemento_elemendeportivo = db.Column(db.ForeignKey('tipoelemento.idtipoelemento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idestado_elemendeportivo = db.Column(db.ForeignKey('estado.idestado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idmarca_elemendeportivo = db.Column(db.ForeignKey('marca.idmarca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    fecharegistro = db.Column(db.Date, nullable=False)

    espacio = db.relationship('Espacio', primaryjoin='Elemendeportivo.codespacio_elemendeportivo == Espacio.codespacio', backref='elemendeportivoes')
    estado = db.relationship('Estado', primaryjoin='Elemendeportivo.idestado_elemendeportivo == Estado.idestado', backref='elemendeportivoes')
    marca = db.relationship('Marca', primaryjoin='Elemendeportivo.idmarca_elemendeportivo == Marca.idmarca', backref='elemendeportivoes')
    tipoelemento = db.relationship('Tipoelemento', primaryjoin='Elemendeportivo.idtipoelemento_elemendeportivo == Tipoelemento.idtipoelemento', backref='elemendeportivoes')



class Empleado(db.Model):
    __tablename__ = 'empleado'

    codempleado = db.Column(db.String(4), primary_key=True)
    nomempleado = db.Column(db.String(20), nullable=False)
    apellempleado = db.Column(db.String(20), nullable=False)
    fecharegistro = db.Column(db.Date, nullable=False)
    correoud = db.Column(db.String(30), nullable=False)



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



class Equipo(db.Model):
    __tablename__ = 'equipo'

    conseequipo = db.Column(db.Integer, primary_key=True)
    iddeporte_equipo = db.Column(db.ForeignKey('deporte.iddeporte', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    codempleado_equipo = db.Column(db.ForeignKey('empleado.codempleado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    fecharesol = db.Column(db.Date, nullable=False)

    empleado = db.relationship('Empleado', primaryjoin='Equipo.codempleado_equipo == Empleado.codempleado', backref='equipoes')
    deporte = db.relationship('Deporte', primaryjoin='Equipo.iddeporte_equipo == Deporte.iddeporte', backref='equipoes')



class Espacio(db.Model):
    __tablename__ = 'espacio'

    codespacio = db.Column(db.String(2), primary_key=True)
    idtipoespacio_espacio = db.Column(db.ForeignKey('tipoespacio.idtipoespacio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    codespacio_espacio = db.Column(db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nomespacio = db.Column(db.String(30), nullable=False)

    parent = db.relationship('Espacio', remote_side=[codespacio], primaryjoin='Espacio.codespacio_espacio == Espacio.codespacio', backref='espacios')
    tipoespacio = db.relationship('Tipoespacio', primaryjoin='Espacio.idtipoespacio_espacio == Tipoespacio.idtipoespacio', backref='espacios')
    deporte = db.relationship('Deporte', secondary='espacio_deporte', backref='espacios')



t_espacio_deporte = db.Table(
    'espacio_deporte',
    db.Column('codespacio_espaciodeporte', db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True),
    db.Column('iddeporte_espaciodeporte', db.ForeignKey('deporte.iddeporte', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
)



class Estado(db.Model):
    __tablename__ = 'estado'

    idestado = db.Column(db.String(2), primary_key=True)
    descestado = db.Column(db.String(20), nullable=False)



class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    codestu = db.Column(db.String(12), primary_key=True)
    codespacio_estudiante = db.Column(db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nomestu = db.Column(db.String(30), nullable=False)
    apelestu = db.Column(db.String(30), nullable=False)
    fecharegestu = db.Column(db.Date, nullable=False)
    correoudestu = db.Column(db.String(30), nullable=False)
    fechanacestu = db.Column(db.Date, nullable=False)

    espacio = db.relationship('Espacio', primaryjoin='Estudiante.codespacio_estudiante == Espacio.codespacio', backref='estudiantes')



class Hora(db.Model):
    __tablename__ = 'hora'

    idhora = db.Column(db.String(5), primary_key=True)



class Inscritopraclibre(db.Model):
    __tablename__ = 'inscritopraclibre'

    consecprogra_inscritopraclibre = db.Column(db.ForeignKey('programacion.consecprogra', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    consecpract = db.Column(db.Integer, primary_key=True, nullable=False)
    codempleado_inscritopraclibre = db.Column(db.ForeignKey('empleado.codempleado', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    codestu_inscritopraclibre = db.Column(db.ForeignKey('estudiante.codestu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    empleado = db.relationship('Empleado', primaryjoin='Inscritopraclibre.codempleado_inscritopraclibre == Empleado.codempleado', backref='inscritopraclibres')
    estudiante = db.relationship('Estudiante', primaryjoin='Inscritopraclibre.codestu_inscritopraclibre == Estudiante.codestu', backref='inscritopraclibres')
    programacion = db.relationship('Programacion', primaryjoin='Inscritopraclibre.consecprogra_inscritopraclibre == Programacion.consecprogra', backref='inscritopraclibres')



class Marca(db.Model):
    __tablename__ = 'marca'

    idmarca = db.Column(db.String(3), primary_key=True)
    nommarca = db.Column(db.String(20), nullable=False)



class Miembroequipo(db.Model):
    __tablename__ = 'miembroequipo'

    conseequipo_miembroequipo = db.Column(db.ForeignKey('equipo.conseequipo', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    itemmiembro = db.Column(db.Integer, primary_key=True, nullable=False)
    codestu_miembroequipo = db.Column(db.ForeignKey('estudiante.codestu', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    estudiante = db.relationship('Estudiante', primaryjoin='Miembroequipo.codestu_miembroequipo == Estudiante.codestu', backref='miembroequipoes')
    equipo = db.relationship('Equipo', primaryjoin='Miembroequipo.conseequipo_miembroequipo == Equipo.conseequipo', backref='miembroequipoes')



class Periodo(db.Model):
    __tablename__ = 'periodo'

    idperiodo = db.Column(db.String(5), primary_key=True)



class Prestamo(db.Model):
    __tablename__ = 'prestamo'
    __table_args__ = (
        db.ForeignKeyConstraint(['consecprogra_resp_prest', 'consecres_asisresp_prest', 'consecasisres_prestamo'], ['asistirresponsable.consecprogra_responsable', 'asistirresponsable.consecres_asistirresponsable', 'asistirresponsable.consecasisres'], ondelete='RESTRICT', onupdate='RESTRICT'),
        db.Index('asistirresponsable_prestamo_fk', 'consecprogra_resp_prest', 'consecres_asisresp_prest', 'consecasisres_prestamo')
    )

    consecprestamo = db.Column(db.Integer, primary_key=True)
    consecprogra_resp_prest = db.Column(db.Integer, nullable=False)
    consecres_asisresp_prest = db.Column(db.Integer, nullable=False)
    consecasisres_prestamo = db.Column(db.Integer, nullable=False)
    consecelemento_prestamo = db.Column(db.ForeignKey('elemendeportivo.consecelemento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    elemendeportivo = db.relationship('Elemendeportivo', primaryjoin='Prestamo.consecelemento_prestamo == Elemendeportivo.consecelemento', backref='prestamoes')
    asistirresponsable = db.relationship('Asistirresponsable', primaryjoin='and_(Prestamo.consecprogra_resp_prest == Asistirresponsable.consecprogra_responsable, Prestamo.consecres_asisresp_prest == Asistirresponsable.consecres_asistirresponsable, Prestamo.consecasisres_prestamo == Asistirresponsable.consecasisres)', backref='prestamoes')



class Programacion(db.Model):
    __tablename__ = 'programacion'

    consecprogra = db.Column(db.Integer, primary_key=True)
    codespacio_programacion = db.Column(db.ForeignKey('espacio.codespacio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    iddeporte_programacion = db.Column(db.ForeignKey('deporte.iddeporte', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idperiodo_programacion = db.Column(db.ForeignKey('periodo.idperiodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idactividad_programacion = db.Column(db.ForeignKey('actividad.idactividad', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idhorainicio_programacion = db.Column(db.ForeignKey('hora.idhora', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    idhorafin_programacion = db.Column(db.ForeignKey('hora.idhora', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    iddia_programacion = db.Column(db.ForeignKey('dia.iddia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cupo = db.Column(db.Integer, nullable=False)
    noinscrito = db.Column(db.Integer, nullable=False)

    espacio = db.relationship('Espacio', primaryjoin='Programacion.codespacio_programacion == Espacio.codespacio', backref='programacions')
    actividad = db.relationship('Actividad', primaryjoin='Programacion.idactividad_programacion == Actividad.idactividad', backref='programacions')
    deporte = db.relationship('Deporte', primaryjoin='Programacion.iddeporte_programacion == Deporte.iddeporte', backref='programacions')
    dia = db.relationship('Dia', primaryjoin='Programacion.iddia_programacion == Dia.iddia', backref='programacions')
    hora = db.relationship('Hora', primaryjoin='Programacion.idhorafin_programacion == Hora.idhora', backref='hora_programacions')
    hora1 = db.relationship('Hora', primaryjoin='Programacion.idhorainicio_programacion == Hora.idhora', backref='hora_programacions_0')
    periodo = db.relationship('Periodo', primaryjoin='Programacion.idperiodo_programacion == Periodo.idperiodo', backref='programacions')



class Responsable(db.Model):
    __tablename__ = 'responsable'

    consecprogra_responsable = db.Column(db.ForeignKey('programacion.consecprogra', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    consecres = db.Column(db.Integer, primary_key=True, nullable=False)
    codempleado_responsable = db.Column(db.ForeignKey('empleado.codempleado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    codestu_responsable = db.Column(db.ForeignKey('estudiante.codestu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    idrol_responsable = db.Column(db.ForeignKey('rol.idrol', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    fechaini = db.Column(db.Date, nullable=False)
    fechafin = db.Column(db.Date, nullable=False)

    empleado = db.relationship('Empleado', primaryjoin='Responsable.codempleado_responsable == Empleado.codempleado', backref='responsables')
    estudiante = db.relationship('Estudiante', primaryjoin='Responsable.codestu_responsable == Estudiante.codestu', backref='responsables')
    programacion = db.relationship('Programacion', primaryjoin='Responsable.consecprogra_responsable == Programacion.consecprogra', backref='responsables')
    rol = db.relationship('Rol', primaryjoin='Responsable.idrol_responsable == Rol.idrol', backref='responsables')



class Rol(db.Model):
    __tablename__ = 'rol'

    idrol = db.Column(db.String(1), primary_key=True)
    descrol = db.Column(db.String(20), nullable=False)



class Tipoelemento(db.Model):
    __tablename__ = 'tipoelemento'

    idtipoelemento = db.Column(db.String(2), primary_key=True)
    desctipoelemento = db.Column(db.String(40), nullable=False)



class Tipoespacio(db.Model):
    __tablename__ = 'tipoespacio'

    idtipoespacio = db.Column(db.String(2), primary_key=True)
    desctipoespacio = db.Column(db.String(30), nullable=False)
