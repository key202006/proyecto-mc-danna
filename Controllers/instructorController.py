from flask import jsonify,request
from Services.instructorService import instructorService
from Services.personaService import personaService


class InstructorController:

    def show():
        data = instructorService.show()
        return jsonify(data), 200

    def add():
                data = request.get_json(silent=True)
                if data is None :
                    return jsonify({"mensaje": "json invalido"}), 400
                campo_req = ("especialidad","per_id")
                faltantes = [W for W in campo_req if W not in data]
        
                if len(faltantes) > 0 :
                    return jsonify({"mensaje":f"faltan parametros {faltantes}"}), 400


                if not isinstance(data.get("especialidad"), str):
                    return jsonify({"mensaje":"la especialidad debe ser cadena de texto"}), 400
                

                if not isinstance(data.get("per_id"), int):
                    return jsonify({"mensaje": "el id de la persona debe ser un entero"}), 400

                if personaService.get_by_id(data["per_id"]) == "No se encontro la persona ":
                            return jsonify({"mensaje": "la persona no existe"}), 400


                x = instructorService.add(data)
                return jsonify(x), 201
                
    def delete(uuid):
        x = instructorService.delete(uuid)
        if x == 200:
            return jsonify ({"mensaje": f"se elimino el instructor con uuid :{uuid}"}), 200
        else:
            return jsonify ({"mensaje": f"no se encontro el instructor con el uuid :{uuid}"}), 404 


        


    def update(uuid):
        data = request.get_json()
        campos_req = ['especialidad', 'per_id']
        faltantes = [w for w in campos_req if w not in data]
    
        if len(faltantes) > 0:
            return jsonify({"faltan campos": faltantes}), 400
    
        x = instructorService.get_by_id(data["per_id"])
        if len(x) > 0:
            return jsonify({"no existe la persona": x}), 400
    
        x = instructorService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo el instructor con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el instructor con uuid: {uuid}"}), 404