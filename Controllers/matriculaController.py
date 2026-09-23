from flask import jsonify, request
from Services.matriculaService import Matricula


class matriculaController:

    def show():
        data = Matricula.show()

    def add():
        data = request.get_json()
        campos_req = ["MAT_ESTADO", "MAT_FECHA_INCRIPCION", "MAT_CUR_ID", "MAT_APR_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
                #data = aprendizService.add()
            return jsonify(data), 201
    
        
    def delete(uuid):
        x = Matricula.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino la matricula con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la matricula con uuid: {uuid}"}), 404