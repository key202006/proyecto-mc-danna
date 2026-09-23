from flask import jsonify, request
from Services.imparteService import Imparte


class imparteController:

    def show():
        data = Imparte.show()

    def add():
        data = request.get_json()
        campos_req = ["IMP_ROL", "IMP_FECHA_ASIGNACION", "IMP_CUR_ID", "IMP_INS_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
                #data = aprendizService.add()
            return jsonify(data), 201
    def delete(uuid):
        x = Imparte.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino la imparticion  con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la imparticion con uuid: {uuid}"}), 404