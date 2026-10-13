from flask import jsonify, request
from Services.aprendicesService import aprendizService
from Services.persona import personaService


class aprendizController:

    def show():
        data = aprendizService.show()
        return jsonify([ x.to_dict() for x in data ]), 200

    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["APR_FECHA_NAC", "APR_PER_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400

        if len(personaService.get_by_id(data["APR_PER_ID"])) == 0:
            return jsonify({"mensaje": "no existe la persona", "APR_PER_ID": data["APR_PER_ID"]}), 400

        respuesta = aprendizService.add(data)
        return jsonify(respuesta), 201

    def update(uuid):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["APR_FECHA_NAC", "APR_PER_ID"]
        if len([ x for x in campos_req if x in data ]) == 0:
            return jsonify({"mensaje": "envie al menos uno de estos campos", "campos": campos_req}), 400
        if "APR_PER_ID" in data and len(personaService.get_by_id(data["APR_PER_ID"])) == 0:
            return jsonify({"mensaje": "no existe la persona", "APR_PER_ID": data["APR_PER_ID"]}), 400

        x = aprendizService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo el aprendiz con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el aprendiz con uuid: {uuid}"}), 404

    def get_one(uuid):
        # datos del aprendiz con sus cursos, notas y promedio
        data = aprendizService.get_boletin(uuid)
        if data is None:
            return jsonify({"mensaje": f"no se encontro el aprendiz con uuid: {uuid}"}), 404
        return jsonify(data), 200

    def delete(uuid):
        x = aprendizService.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino el aprendiz con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el aprendiz con uuid: {uuid}"}), 404
