from flask import jsonify, request
from Services.instructorService import instructorService
from Services.persona import personaService


class instructorController:

    def show():
        data = instructorService.show()
        return jsonify([ x.to_dict() for x in data ]), 200

    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["INS_ESPECIALIDAD", "INS_PER_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400

        if len(personaService.get_by_id(data["INS_PER_ID"])) == 0:
            return jsonify({"mensaje": "no existe la persona", "INS_PER_ID": data["INS_PER_ID"]}), 400

        respuesta = instructorService.add(data)
        return jsonify(respuesta), 201

    def update(uuid):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["INS_ESPECIALIDAD", "INS_PER_ID"]
        if len([ x for x in campos_req if x in data ]) == 0:
            return jsonify({"mensaje": "envie al menos uno de estos campos", "campos": campos_req}), 400
        if "INS_PER_ID" in data and len(personaService.get_by_id(data["INS_PER_ID"])) == 0:
            return jsonify({"mensaje": "no existe la persona", "INS_PER_ID": data["INS_PER_ID"]}), 400

        x = instructorService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo el instructor con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el instructor con uuid: {uuid}"}), 404

    def delete(uuid):
        x = instructorService.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino el instructor con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el instructor con uuid: {uuid}"}), 40
