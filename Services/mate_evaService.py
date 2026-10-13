from flask import current_app
from Models.MatEva import MatEva
import uuid


class matevaService:

    def show():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT MATE_ID, MATE_UUID, MATE_NOTA, MATE_EVA_ID, MATE_MAT_ID FROM T_MAT_EVA")
        data = c.fetchall()
        c.close()
        return [ MatEva(x[0], x[1], x[2], x[3], x[4]) for x in data ]

    def add(data):
        nuevo_uuid = str(uuid.uuid4())  # genera un uuid
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_MAT_EVA (MATE_UUID, MATE_NOTA, MATE_EVA_ID, MATE_MAT_ID)
                 VALUES (%s, %s, %s, %s)"""  # consulta parametrizada
        c.execute(sql, (nuevo_uuid, data['MATE_NOTA'], data['MATE_EVA_ID'], data['MATE_MAT_ID']))
        current_app.mysql.connection.commit()  # guarda los cambios
        id = c.lastrowid
        c.close()
        respuesta = {"MATE_ID": id, "MATE_UUID": nuevo_uuid}
        respuesta.update(data)
        return respuesta

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT MATE_ID FROM T_MAT_EVA WHERE MATE_UUID = %s", [uuid])
        if c.fetchone() is None:
            c.close()
            return 404
        campos = ["MATE_NOTA", "MATE_EVA_ID", "MATE_MAT_ID"]
        cambios = [ k for k in campos if k in data ]
        sql = "UPDATE T_MAT_EVA SET " + ", ".join([ k + " = %s" for k in cambios ]) + " WHERE MATE_UUID = %s"
        c.execute(sql, [ data[k] for k in cambios ] + [uuid])
        current_app.mysql.connection.commit()
        c.close()
        return 200

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_MAT_EVA WHERE MATE_UUID = %s", [uuid])
        current_app.mysql.connection.commit()
        if c.rowcount > 0:
            codigo = 200
        else:
            codigo = 404
        c.close()
        return codigo
