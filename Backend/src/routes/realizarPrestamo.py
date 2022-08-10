from models import db
from models.elemendeportivoModel import Elemendeportivo,ElemendeportivoSchema
from models.empleadocargoModel import EmpleadoCargo,EmpleadoCargoSchema
from models.empleadoModel import Empleado,EmpleadoSchema
from flask import request
from flask_restful import Resource
from sqlalchemy import and_
from datetime import date ,datetime

from models.responsableModel import Responsable,ResponsableSchema

empleadocargo_schema=EmpleadoCargoSchema()
empleado_schema=EmpleadoSchema()
responsable_schema=ResponsableSchema(many=True)
elementodeportivo_schema=ElemendeportivoSchema(many=True)

class RealizarPrestamoResource(Resource):
    def post(self):
        fecha=date.today()
        hora=datetime.now().hour
        hora=11
        nom_doc=nom_doc.upper()
        apell_doc=apell_doc.upper()
        docente=Empleado.query.filter(Empleado.nomempleado.contains(nom_doc)).filter(Empleado.apellempleado.contains(apell_doc)).first()
        if docente is None:
            return {}, 404
        docente_json=empleado_schema.dump(docente)
        code_emp=docente_json["codempleado"]
        docente_info=EmpleadoCargo.query.filter_by(codempleado_empleadocargo=code_emp,idcargo_empleadocargo="2",fechafincar=None).first()
        if docente_info is None:
            return {}, 404
        responsable=Responsable.query.filter_by(codempleado_responsable=code_emp).filter(and_(fecha>=Responsable.fechaini,Responsable.fechafin>=fecha)).all()
        programacion_responsable=responsable_schema.dump(responsable)
        cursos=[]
        for prog in programacion_responsable:
            if prog['programacion']['actividad']['idactividad'] == 'CU' and hora>=int(prog['programacion']['hora1']['idhora']) and int(prog['programacion']['hora']['idhora'])>=hora:
                elementos_curso=[]
                elementos=Elemendeportivo.query.filter_by(codespacio_elemendeportivo=prog['programacion']['espacio']['codespacio'],idestado_elemendeportivo="1").all()
                elementos=elementodeportivo_schema.dump(elementos)
                print(elementos)
                for elemento in elementos:
                    print(elemento)
                    deportes_elemento=elemento['espacio']['deporte']
                    for deporte in deportes_elemento:
                        if deporte['iddeporte'] == prog['programacion']['deporte']['iddeporte']:
                            elementos_curso.append(elemento)
                            break
                prog['elementos']=elementos_curso
                cursos.append(prog)
            else:
                print("no esta dentro de la hora")
        if not cursos:
            return {"info_docente":empleadocargo_schema.dump(docente_info),"fecha":fecha.strftime("%d-%m-%Y"), "hora":hora}
        return {"info_docente":empleadocargo_schema.dump(docente_info),"Cursos":cursos,"fecha":fecha.strftime("%d-%m-%Y"), "hora":hora}