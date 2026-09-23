from flask import jsonify, request
from Services.evaluacionService import evaluacion


class evaluacionController:

    def show():
        data = evaluacion.show()

    def add():
        data = request.get_json()
        campos_req = ["EVA_NOMBRE", "EVA_CODIGO", "EVA_PORCENTAJE", "EVA_FECHA"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
                #data = aprendizService.add()
            return jsonify(data), 201
    def delete(uuid):
        x = evaluacion.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino la evaluacion con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la evaluacion con uuid: {uuid}"}), 404