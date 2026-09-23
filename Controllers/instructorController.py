from flask import jsonify, request
from Services.instructorService import Instructor
from Services.persona import Persona


class instructorController:

    def show():
        data = Instructor.show()

    
    def add():
        data = request.get_json()
        campos_req = ["INS_ESPECIALIDAD", "INS_PER_ID"]
        faltantes = [ w for w in campos_req if w not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
            
        x = Persona.get_by_id(data["INS_PER_ID"])
        if len(x) > 0:
            return jsonify({"no existe la persona": x}), 400
        #data = aprendizService.add()
        return jsonify(data), 201
    
    def delete(uuid):
        x = Instructor.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino el instructor con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el instructor con uuid: {uuid}"}), 404