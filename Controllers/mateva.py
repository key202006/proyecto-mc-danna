from flask import jsonify, request
from Services.matevaService import matevaService


class matEvaController:

    def show():
        data = matevaService.show()
        return jsonify([ x.to_dict() for x in data ]), 200

    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["MATE_NOTA", "MATE_EVA_ID", "MATE_MAT_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400

        respuesta = matevaService.add(data)
        return jsonify(respuesta), 201

    def update(uuid):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["MATE_NOTA", "MATE_EVA_ID", "MATE_MAT_ID"]
        if len([ x for x in campos_req if x in data ]) == 0:
            return jsonify({"mensaje": "envie al menos uno de estos campos", "campos": campos_req}), 400

        x = matevaService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo la mat_eva con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la mat_eva con uuid: {uuid}"}), 404

    def delete(uuid):
        x = matevaService.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino la mat_eva con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la mat_eva con uuid: {uuid}"}), 404
