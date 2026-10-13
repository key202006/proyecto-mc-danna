from flask import jsonify,request
from Services.personaService import personaService


class PersonaController:

    def show():
        data = personaService.show()
        return jsonify(data), 200

    def add():
                data = request.get_json(silent=True)
                if data is None :
                    return jsonify({"mensaje": "json invalido"}), 400
                campo_req = ("pri_nombre","seg_nombre","pri_apellido","seg_apellido","documento")
                faltantes = [W for W in campo_req if W not in data]
        
                if len(faltantes) > 0 :
                    return jsonify({"mensaje":f"faltan parametros {faltantes}"}), 400




                if not isinstance(data.get("pri_nombre"), str):
                    return jsonify({"mensaje": "el primer nombre debe ser cadena de texto"}), 400  
                 
                if not isinstance(data.get("seg_nombre"), str):
                    return jsonify({"mensaje": "el segundo nombre debe ser cadena de texto"}), 400  
                 
                if not isinstance(data.get("pri_apellido"), str):
                    return jsonify({"mensaje": "el primer apellido debe ser cadena de texto"}), 400 
                  
                if not isinstance(data.get("seg_apellido"), str):
                    return jsonify({"mensaje": "el segundo apellido debe ser cadena de texto"}), 400

                if not isinstance(data.get("documento"), int):
                    return jsonify({"mensaje": "el docuemnto debe ser numero entero"}), 400


                
                x = personaService.add(data)
                return jsonify(x),201
                                
                                
                                
    def delete(uuid):
        x = personaService.delete(uuid)
        if x == 200:
            return jsonify ({"mensaje": f"se elimino la persona con el uuid:{uuid}"}),200
        else:
            return jsonify({"mensaje": f"no se encontro la persona con el uuid{uuid}"}),404

        



    def update(uuid):
                data = request.get_json()
                campos_req = ['pri_nombre', 'seg_nombre', 'pri_apellido', 'seg_apellido', 'documento']
                faltantes = [w for w in campos_req if w not in data]
        
                if len(faltantes) > 0:
                    return jsonify({"faltan campos": faltantes}), 400
        
                x = personaService.update(uuid, data)
                if x == 200:
                    return jsonify({"mensaje": f"se actualizo la persona con uuid: {uuid}"}), 200
                else:
                    return jsonify({"mensaje": f"no se encontro la persona con uuid: {uuid}"}), 404

    