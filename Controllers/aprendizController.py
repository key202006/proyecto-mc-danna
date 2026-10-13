
from flask import jsonify,request
from Services.aprendizService import aprendizService
from Services.personaService import personaService


class aprendizController:

    def show():
        data = aprendizService.show()
        return jsonify(data), 200

    def add():
        data = request.get_json(silent=True)
        if data is None :
            return jsonify({"mensaje": "json invalido"}), 400
        campo_req = ("fecha_nac","per_id")
        faltantes = [W for W in campo_req if W not in data]

        if len(faltantes) > 0 :
            return jsonify({"mensaje":f"faltan parametros {faltantes}"}), 400

        if not isinstance(data.get("per_id"), int):
            return jsonify({"mensaje": "el id de la persona debe ser un entero"}), 400  

        if not isinstance(data.get("fecha_nac"), str) or not re.match(r"^\d{4}-\d{2}-\d{2}$", data.get("fecha_nac")):
            return jsonify({"mensaje": "el formato de fecha es invalido  debe ser yyyy-mm-dd"}), 400
        
        if personaService.get_by_id(data["per_id"]) == "No se encontro la persona ":
            return jsonify({"mensaje": "la persona no existe"}), 400

        x = aprendizService.add(data)
        return jsonify(x), 201

    def delete(uuid):
        x = aprendizService.delete(uuid)
        if x == 200:
            return jsonify ({"mensaje": f"se elimino el aprendiz con uuid :{uuid}"}), 200
        else:
            return jsonify ({"mensaje": f"no se encontro el recurso uuid :{uuid}"}), 404

    def update(uuid):
        data = request.get_json()
        campos_req = ['fecha_nac','per_id']
        faltantes = [w for w in campos_req if w not in data]

        if len(faltantes) > 0:
            return jsonify({"faltan campos": faltantes}), 400

        x = personaService.get_by_id(data["per_id"])
        if x is None :
            return jsonify({"no existe la persona": x}), 400

        x = aprendizService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo el aprendiz con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el aprendiz con uuid: {uuid}"}), 404