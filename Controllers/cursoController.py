from flask import jsonify, request
from Services.cursoService import cursoService


class cursoController:

    def show():
        data = cursoService.show()
        return jsonify([ x.to_dict() for x in data ]), 200

    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["CUR_NOMBRE", "CUR_CODIGO", "CUR_DURACION", "CUR_COSTO", "CUR_DESCRIPCION"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400

        respuesta = cursoService.add(data)
        return jsonify(respuesta), 201

    def update(uuid):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "se esperaba un JSON en el cuerpo"}), 400
        campos_req = ["CUR_NOMBRE", "CUR_CODIGO", "CUR_DURACION", "CUR_COSTO", "CUR_DESCRIPCION"]
        if len([ x for x in campos_req if x in data ]) == 0:
            return jsonify({"mensaje": "envie al menos uno de estos campos", "campos": campos_req}), 400

        x = cursoService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo el curso con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el curso con uuid: {uuid}"}), 404

    def delete(uuid):
        x = cursoService.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino el curso con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el curso con uuid: {uuid}"}), 404
