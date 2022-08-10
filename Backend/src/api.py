from flask import Flask
from models import db, ma
from flask_restful import Api

from routes.actividadRoute import ActividadesResource,ActividadResource
from routes.asismiembroequipoRoute import AsismiembroequipoResource,AsismiembroequiposResource
from routes.asistirresponsableRoute import AsistirresponsableResource,AsistirresponsablesResource
from routes.cargoRoute import CargoResource,CargosResource
from routes.deporteRoute import DeporteResource,DeportesResource
from routes.diaRoute import DiaResource, DiasResource
from routes.elemendeportivoRoute import ElemendeportivoResource,ElemendeportivosResource
from routes.empleadocargoRoute import EmpleadoCargoResource, EmpleadoCargosResource
from routes.empleadoRoute import EmpleadoResource, EmpleadosResource
from routes.equipoRoute import EquipoResource, EquiposResource
from routes.espacioRoute import EspacioResource, EspaciosResource
from routes.estadoRoute import EstadoResource, EstadosResource
from routes.estudianteRoute import EstudianteResource, EstudiantesResource
from routes.horaRoute import HoraResource, HorasResource
from routes.inscritopraclibreRoute import InscritopraclibreResource, InscritopraclibresResource
from routes.marcaRoute import MarcaResource, MarcasResource
from routes.miembroequipoRoute import MiembroequipoResource, MiembroequiposResource
from routes.periodoRoute import PeriodoResource, PeriodosResource
from routes.prestamoRoute import PrestamoResource, PrestamosResource
from routes.programacionRoute import ProgramacionResource, ProgramacionsResource
from routes.responsableRoute import ResponsableResource, ResponsablesResource
from routes.rolRoute import RolResource, RolsResource
from routes.tipoelementoRoute import TipoelementoResource, TipoelementosResource
from routes.tipoespacioRoute import TipoespaciosResource, TipoespacioResource

from routes.loginAux import LoginAuxResource
from routes.asistenciaDocente import AsistenciaDocenteResource
## Declaracion inicial

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://cdrodriguezl:cdrodriguezl@localhost:1521/xe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma.init_app(app)
api = Api(app)

api.add_resource(ActividadesResource, '/actividad')
api.add_resource(ActividadResource,'/actividad/<string:actividad_id>')

api.add_resource(AsismiembroequiposResource, '/asismiembroequipo')
api.add_resource(AsismiembroequipoResource,'/asismiembroequipo/<int:asismiembroequipo_id>')

api.add_resource(AsistirresponsablesResource, '/asistirresponsable')
api.add_resource(AsistirresponsableResource,'/asistirresponsable/<int:asistirresponsable_id>')

api.add_resource(CargosResource, '/cargo')
api.add_resource(CargoResource,'/cargo/<string:cargo_id>')

api.add_resource(DeportesResource, '/deporte')
api.add_resource(DeporteResource,'/deporte/<string:deporte_id>')

api.add_resource(DiasResource, '/dia')
api.add_resource(DiaResource,'/dia/<string:dia_id>')

api.add_resource(ElemendeportivosResource, '/elemendeportivo')
api.add_resource(ElemendeportivoResource,'/elemendeportivo/<int:elemendeportivoResource_id>')

api.add_resource(EmpleadoCargosResource, '/empleadocargo')
api.add_resource(EmpleadoCargoResource,'/empleadocargo/<int:empleadocargo_id>')

api.add_resource(EmpleadosResource, '/empleado')
api.add_resource(EmpleadoResource,'/empleado/<string:empleado_id>')

api.add_resource(EquiposResource, '/equipo')
api.add_resource(EquipoResource,'/equipo/<int:equipo_id>')

api.add_resource(EspaciosResource, '/espacio')
api.add_resource(EspacioResource,'/espacio/<string:espacio_id>')

api.add_resource(EstadosResource, '/estado')
api.add_resource(EstadoResource,'/estado/<string:estado_id>')

api.add_resource(EstudiantesResource, '/estudiante')
api.add_resource(EstudianteResource,'/estudiante/<string:estudiante_id>')

api.add_resource(HorasResource, '/hora')
api.add_resource(HoraResource,'/hora/<string:hora_id>')

api.add_resource(InscritopraclibresResource, '/inscritopraclibres')
api.add_resource(InscritopraclibreResource,'/inscritopraclibres/<int:inscritopraclibres_id>')

api.add_resource(MarcasResource, '/marca')
api.add_resource(MarcaResource,'/marca/<string:marca_id>')

api.add_resource(MiembroequiposResource, '/miembroequipo')
api.add_resource(MiembroequipoResource,'/miembroequipo/<int:miembroequipo_id>')

api.add_resource(PeriodosResource, '/periodo')
api.add_resource(PeriodoResource,'/periodo/<string:periodo_id>')

api.add_resource(PrestamosResource, '/prestamo')
api.add_resource(PrestamoResource,'/prestamo/<int:prestamo_id>')

api.add_resource(ProgramacionsResource, '/programacion')
api.add_resource(ProgramacionResource,'/programacion/<int:programacion_id>')

api.add_resource(ResponsablesResource, '/responsable')
api.add_resource(ResponsableResource,'/responsable/<int:responsable_id>')

api.add_resource(RolsResource, '/rol')
api.add_resource(RolResource,'/rol/<string:rol_id>')

api.add_resource(TipoelementosResource, '/tipoelemento')
api.add_resource(TipoelementoResource,'/tipoelemento/<string:tipoelemento_id>')

api.add_resource(TipoespaciosResource, '/tipoespacio')
api.add_resource(TipoespacioResource,'/tipoespacio/<string:tipoespacio_id>')

api.add_resource(LoginAuxResource,'/login/<string:code_emp>')

api.add_resource(AsistenciaDocenteResource,'/asistencia_docente/<string:nom_doc>/<string:apell_doc>')

if __name__ == '__main__':
    app.run(debug=True)