from flask import jsonify, request
from Services.persona import Persona


class personaController:

    def show():
        data = Persona.show()

    def add():
        data = request.get_json()
        campos_req = ["PER_PRI_NOMBRE", "PER_SEG_NOMBRE", "PER_PRI_APELLIDO", "PER_SEG_APELLIDO", "PER_DOCUMENTO"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
                #data = aprendizService.add()
            return jsonify(data), 201
    
        
    def delete(uuid):
        x = Persona.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino la persona con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la persona con uuid: {uuid}"}), 404