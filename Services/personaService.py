from flask import current_app
from Models.Persona import Persona
import uuid


class personaService:

    def show():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT PER_ID, PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOCUMENTO FROM T_PERSONA")
        data = c.fetchall()
        c.close()
        return [ Persona(x[0], x[1], x[2], x[3], x[4], x[5], x[6]) for x in data ]

    def add(data):
        nuevo_uuid = str(uuid.uuid4())  # genera un uuid
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_PERSONA (PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOCUMENTO)
                 VALUES (%s, %s, %s, %s, %s, %s)"""  # consulta parametrizada
        c.execute(sql, (nuevo_uuid, data['PER_PRI_NOMBRE'], data['PER_SEG_NOMBRE'], data['PER_PRI_APELLIDO'], data['PER_SEG_APELLIDO'], data['PER_DOCUMENTO']))
        current_app.mysql.connection.commit()  # guarda los cambios
        id = c.lastrowid
        c.close()
        respuesta = {"PER_ID": id, "PER_UUID": nuevo_uuid}
        respuesta.update(data)
        return respuesta

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT PER_ID FROM T_PERSONA WHERE PER_UUID = %s", [uuid])
        if c.fetchone() is None:
            c.close()
            return 404
        campos = ["PER_PRI_NOMBRE", "PER_SEG_NOMBRE", "PER_PRI_APELLIDO", "PER_SEG_APELLIDO", "PER_DOCUMENTO"]
        cambios = [ k for k in campos if k in data ]
        sql = "UPDATE T_PERSONA SET " + ", ".join([ k + " = %s" for k in cambios ]) + " WHERE PER_UUID = %s"
        c.execute(sql, [ data[k] for k in cambios ] + [uuid])
        current_app.mysql.connection.commit()
        c.close()
        return 200

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_PERSONA WHERE PER_UUID = %s", [uuid])
        current_app.mysql.connection.commit()
        if c.rowcount > 0:
            codigo = 200
        else:
            codigo = 404
        c.close()
        return codigo

    def get_by_id(id):
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT PER_ID, PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOCUMENTO FROM T_PERSONA WHERE PER_ID = %s", [id])
        data = c.fetchall()
        c.close()
        return [ Persona(x[0], x[1], x[2], x[3], x[4], x[5], x[6]) for x in data ]
