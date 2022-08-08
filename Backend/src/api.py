from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

## Declaracion inicial

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://camilo:jc_o980109ML@localhost:1521/xe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

### Definicion de los modelos y esquemas

class Actividad(db.Model):
    IDACTIVIDAD = db.Column(db.String(2), primary_key=True)
    DESCACTIVIDAD = db.Column(db.String(30))

    def __repr__(self):
        return '<Actividad %s>' % self.title


class ActividadSchema(ma.Schema):
    class Meta:
        fields = ("IDACTIVIDAD", "DESCACTIVIDAD")


actividad_schema = ActividadSchema()
actividades_schema = ActividadSchema(many=True)

### Creacion de recursos para la rutas

class ActividadesResource(Resource):
    def get(self):
        actividades=Actividad.query.all()
        return actividades_schema.dump(actividades)

    def post(self):
        new_actividad = Actividad(
            IDACTIVIDAD=request.json['IDACTIVIDAD'],
            DESCACTIVIDAD=request.json['DESCACTIVIDAD']
        )
        db.session.add(new_actividad)
        db.session.commit()
        return actividad_schema.dump(new_actividad)


class ActividadResource(Resource):
    def get(self, actividad_id):
        actividad = Actividad.query.get_or_404(actividad_id)
        return actividad_schema.dump(actividad)

    def patch(self, actividad_id):
        actividad = Actividad.query.get_or_404(actividad_id)

        if 'IDACTIVIDAD' in request.json:
            actividad.IDACTIVIDAD = request.json['IDACTIVIDAD']
        if 'DESCACTIVIDAD' in request.json:
            actividad.DESCACTIVIDAD = request.json['DESCACTIVIDAD']

        db.session.commit()
        return actividad_schema.dump(actividad)

    def delete(self, actividad_id):
        actividad = Actividad.query.get_or_404(actividad_id)
        db.session.delete(actividad)
        db.session.commit()
        return '', 204

### asignacion de rutas

api.add_resource(ActividadesResource, '/actividad')
api.add_resource(ActividadResource,'/actividad/<string:actividad_id>')



if __name__ == '__main__':
    app.run(debug=True)