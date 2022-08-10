from models import db
from models.tipoelementoModel import Tipoelemento,TipoelementoSchema
from flask import request
from flask_restful import Resource

tipoelementos_schema=TipoelementoSchema(many=True)
tipoelemento_schema=TipoelementoSchema()

class TipoelementosResource(Resource):
    def get(self):
        tipoelementos=Tipoelemento.query.all()
        return tipoelementos_schema.dump(tipoelementos)

    def post(self):
        new_tipoelemento = Tipoelemento(
            idtipoelemento=request.json['idtipoelemento'],
            desctipoelemento=request.json['desctipoelemento'],
        )
        db.session.add(new_tipoelemento)
        db.session.commit()
        return tipoelemento_schema.dump(new_tipoelemento)


class TipoelementoResource(Resource):
    def get(self, tipoelemento_id):
        tipoelemento = Tipoelemento.query.get_or_404(tipoelemento_id)
        return tipoelemento_schema.dump(tipoelemento)

    def patch(self, tipoelemento_id):
        tipoelemento = Tipoelemento.query.get_or_404(tipoelemento_id)

        if 'idtipoelemento' in request.json:
            tipoelemento.idtipoelemento = request.json['idtipoelemento']
        if 'desctipoelemento' in request.json:
            tipoelemento.desctipoelemento = request.json['desctipoelemento']

        db.session.commit()
        return tipoelemento_schema.dump(tipoelemento)

    def delete(self, tipoelemento_id):
        tipoelemento = Tipoelemento.query.get_or_404(tipoelemento_id)
        db.session.delete(tipoelemento)
        db.session.commit()
        return '', 204
