from flask import current_app
from Models.Curso import Curso
import uuid


class cursoService:

    def show():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT CUR_ID, CUR_UUID, CUR_NOMBRE, CUR_CODIGO, CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION FROM T_CURSO")
        data = c.fetchall()
        c.close()
        return [ Curso(x[0], x[1], x[2], x[3], x[4], x[5], x[6]) for x in data ]

    def add(data):
        nuevo_uuid = str(uuid.uuid4())  # genera un uuid
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_CURSO (CUR_UUID, CUR_NOMBRE, CUR_CODIGO, CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION)
                 VALUES (%s, %s, %s, %s, %s, %s)"""  # consulta parametrizada
        c.execute(sql, (nuevo_uuid, data['CUR_NOMBRE'], data['CUR_CODIGO'], data['CUR_DURACION'], data['CUR_COSTO'], data['CUR_DESCRIPCION']))
        current_app.mysql.connection.commit()  # guarda los cambios
        id = c.lastrowid
        c.close()
        respuesta = {"CUR_ID": id, "CUR_UUID": nuevo_uuid}
        respuesta.update(data)
        return respuesta

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT CUR_ID FROM T_CURSO WHERE CUR_UUID = %s", [uuid])
        if c.fetchone() is None:
            c.close()
            return 404
        campos = ["CUR_NOMBRE", "CUR_CODIGO", "CUR_DURACION", "CUR_COSTO", "CUR_DESCRIPCION"]
        cambios = [ k for k in campos if k in data ]
        sql = "UPDATE T_CURSO SET " + ", ".join([ k + " = %s" for k in cambios ]) + " WHERE CUR_UUID = %s"
        c.execute(sql, [ data[k] for k in cambios ] + [uuid])
        current_app.mysql.connection.commit()
        c.close()
        return 200

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_CURSO WHERE CUR_UUID = %s", [uuid])
        current_app.mysql.connection.commit()
        if c.rowcount > 0:
            codigo = 200
        else:
            codigo = 404
        c.close()
        return codigo
