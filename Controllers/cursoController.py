from flask import jsonify, request
from Services.cursoService import cursoService

class cursoController:

    def show():
        data = cursoService.show()

    def add():
         data = request.get_json()
         campos_req = ["CUR_NOMBRE", "CUR_CODIGO", "CUR_DURACION", "CUR_COSTO", "CUR_DESCRIPCION"]
         faltantes = [ x for x in campos_req if x not in data ]
         if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
                #data = CursoService.add()
            return jsonify(data), 201
    def delete(uuid):
        x = cursoService.delete(uuid)
        if x == 200:
            return jsonify({"mensaje": f"se elimino el curso con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el curso con uuid: {uuid}"}), 404