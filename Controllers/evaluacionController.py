from flask import jsonify , request
from Services.evaluacionService import evaluacionService
import re


class evaluacionController:

    def show():
        data = evaluacionService.show()
        return jsonify(data), 200

    def add():
            data = request.get_json(silent=True)
            if data is None :
                return jsonify({"respuesta": "json invalido"}), 400
            campo_req = ("nombre","codigo","porcentaje","fecha")
            faltantes = [W for W in campo_req if W not in data]

            if len(faltantes) > 0 :
                return jsonify({"respuesta":f"faltan parametros {faltantes}"}), 400

            if not isinstance(data.get("nombre"), str):
                return jsonify ({"respuesta": "el nombre es una cadena de texto"}),  400

            if not isinstance(data.get("codigo"), int):
                return jsonify ({"respuesta":"el codigo debe ser un  numero entero"}),400

            if not isinstance(data.get("porcentaje"), int):
                return jsonify ({"respuesta": "el porcentaje debe ser un numero entero"}), 400

            if not isinstance(data.get("fecha"), str) or not re.match(r"^\d{4}-\d{2}-\d{2}$", data.get("fecha")):
                return jsonify({"respuesta": "el formato de fecha es invalido  debe ser yyyy-mm-dd"}), 400


            x = evaluacionService.add(data)
             return jsonify({"respuesta": "se registro!!"}),201



    def delete(uuid):
        x = evaluacionService.delete(uuid)
        if x == 200:
             return jsonify ({"respuesta": f"se elimino la evaluacion con uuid:{uuid}"}),200
        else:
            return jsonify({"respuesta": f"no se encontro la evaluacion con el uuid{uuid}"}),404





    def update(uuid):
            data = request.get_json()
            campos_req = ['nombre', 'codigo', 'porcentaje', 'fecha']
            faltantes = [w for w in campos_req if w not in data]
            
            if len(faltantes) > 0:
                return jsonify({"faltan campos": faltantes}), 400
             
                
            x = evaluacionService.update(uuid, data)
            if x == 200:
                    return jsonify({"respuesta": f"se actualizo la evaluacion con uuid: {uuid}"}), 200
            else:
                    return jsonify({"respuesta": f"no se encontro la evaluacion con uuid: {uuid}"}), 404





