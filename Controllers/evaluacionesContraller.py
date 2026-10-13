from flask import jsonify, request
from Services.evaluacionService import evaluacionService


class evaluacionController:

    def show():
        data = evaluacionService.show()
        return jsonify([ x.to_dict() for x in data ]), 200

    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["EVA_NOMBRE", "EVA_CODIGO", "EVA_PORCENTAJE", "EVA_FECHA"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400

        respuesta = evaluacionService.add(data)
        return jsonify(respuesta), 201

    def update(uuid):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["EVA_NOMBRE", "EVA_CODIGO", "EVA_PORCENTAJE", "EVA_FECHA"]
        if len([ x for x in campos_req if x in data ]) == 0:
            return jsonify({"mensaje": "envie al menos uno de estos campos", "campos": campos_req}), 400

        x = evaluacionService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo la evaluacion con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la evaluacion con uuid: {uuid}"}), 404

    def delete(uuid):
        x = evaluacionService.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino la evaluacion con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la evaluacion con uuid: {uuid}"}), 404
