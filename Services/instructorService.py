from flask import current_app
from Models.Instructor import Instructor
import uuid


class instructorService:

    def show():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT INS_ID, INS_UUID, INS_ESPECIALIDAD, INS_PER_ID FROM T_INSTRUCTOR")
        data = c.fetchall()
        c.close()
        return [ Instructor(x[0], x[1], x[2], x[3]) for x in data ]

    def add(data):
        nuevo_uuid = str(uuid.uuid4())  # genera un uuid
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_INSTRUCTOR (INS_UUID, INS_ESPECIALIDAD, INS_PER_ID)
                 VALUES (%s, %s, %s)"""  # consulta parametrizada
        c.execute(sql, (nuevo_uuid, data['INS_ESPECIALIDAD'], data['INS_PER_ID']))
        current_app.mysql.connection.commit()  # guarda los cambios
        id = c.lastrowid
        c.close()
        respuesta = {"INS_ID": id, "INS_UUID": nuevo_uuid}
        respuesta.update(data)
        return respuesta

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT INS_ID FROM T_INSTRUCTOR WHERE INS_UUID = %s", [uuid])
        if c.fetchone() is None:
            c.close()
            return 404
        campos = ["INS_ESPECIALIDAD", "INS_PER_ID"]
        cambios = [ k for k in campos if k in data ]
        sql = "UPDATE T_INSTRUCTOR SET " + ", ".join([ k + " = %s" for k in cambios ]) + " WHERE INS_UUID = %s"
        c.execute(sql, [ data[k] for k in cambios ] + [uuid])
        current_app.mysql.connection.commit()
        c.close()
        return 200

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_INSTRUCTOR WHERE INS_UUID = %s", [uuid])
        current_app.mysql.connection.commit()
        if c.rowcount > 0:
            codigo = 200
        else:
            codigo = 404
        c.close()
        return codigo
