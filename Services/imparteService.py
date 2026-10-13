from flask import current_app
from Models.imparte import Imparte
import uuid


class imparteService:

    def show():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT IMP_ID, IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID FROM T_IMPARTE")
        data = c.fetchall()
        c.close()
        return [ Imparte(x[0], x[1], x[2], x[3], x[4], x[5]) for x in data ]

    def add(data):
        nuevo_uuid = str(uuid.uuid4())  # genera un uuid
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_IMPARTE (IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID)
                 VALUES (%s, %s, %s, %s, %s)"""  # consulta parametrizada
        c.execute(sql, (nuevo_uuid, data['IMP_ROL'], data['IMP_FECHA_ASIGNACION'], data['IMP_CUR_ID'], data['IMP_INS_ID']))
        current_app.mysql.connection.commit()  # guarda los cambios
        id = c.lastrowid
        c.close()
        respuesta = {"IMP_ID": id, "IMP_UUID": nuevo_uuid}
        respuesta.update(data)
        return respuesta

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT IMP_ID FROM T_IMPARTE WHERE IMP_UUID = %s", [uuid])
        if c.fetchone() is None:
            c.close()
            return 404
        campos = ["IMP_ROL", "IMP_FECHA_ASIGNACION", "IMP_CUR_ID", "IMP_INS_ID"]
        cambios = [ k for k in campos if k in data ]
        sql = "UPDATE T_IMPARTE SET " + ", ".join([ k + " = %s" for k in cambios ]) + " WHERE IMP_UUID = %s"
        c.execute(sql, [ data[k] for k in cambios ] + [uuid])
        current_app.mysql.connection.commit()
        c.close()
        return 200

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_IMPARTE WHERE IMP_UUID = %s", [uuid])
        current_app.mysql.connection.commit()
        if c.rowcount > 0:
            codigo = 200
        else:
            codigo = 404
        c.close()
        return codigo
