from flask import jsonify, request
from Services.matevaService import MatEva


class matEvaController:

    def show():
        data = MatEva.show()

    def add():
        data = request.get_json()
        campos_req = ["MATE_MPOTA", "MATE_EVA_ID", "MATE_MAT_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
                #data = aprendizService.add()
            return jsonify(data), 201
    
        
    def delete(uuid):
        x = MatEva.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino la mat_eva con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la mat_eva con uuid: {uuid}"}), 404