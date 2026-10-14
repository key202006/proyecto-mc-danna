from flask import jsonify,request
from Services.mat_evaService import mat_evaService


class mat_evaController:

    def show():
        data = mat_evaService.show()
        return jsonify(data), 200

    def add():
                data = request.get_json(silent=True)
                print(data)
                if data is None :
                    return jsonify({"mensaje": "json invalido"}), 400
                campo_req = ("nota","eva_id","mat_id")
                faltantes = [W for W in campo_req if W not in data]
        
                if len(faltantes) > 0 :
                    return jsonify({"mensaje":f"faltan parametros {faltantes}"}), 400

                print(type(data.get("nota")))
                if not isinstance(data.get("nota"), float):
                    return jsonify({"mensaje":"la nota debe ser numero decimal"}), 400


                if not isinstance(data.get("eva_id"), int):
                    return jsonify({"mensaje":"la eva_id debe ser numero entero"}), 400

                if not isinstance(data.get("mat_id"), int):
                    return jsonify({"mensaje":"la mat_id debe ser numero entero"}), 400


                x = mat_evaService.add(data)
                return jsonify(x),201
                
                
                
    def delete(uuid):
        x = mat_evaService.delete(uuid)
        if x == 200:
             return jsonify ({"mensaje": f"se elimino mat_eva con el uuid:{uuid}"}),200
        else:
             return jsonify({"mensaje": f"no se encontro el mat_eva con el uuid{uuid}"}),404


        

    def update(uuid):
        data = request.get_json()
        campos_req = ['nota', 'eva_id', 'mat_id']
        faltantes = [w for w in campos_req if w not in data]

        if len(faltantes) > 0:
            return jsonify({"faltan campos": faltantes}), 400

        x = mat_evaService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo la evaluacion de la matricula con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la evaluacion de la matricula con uuid: {uuid}"}), 404