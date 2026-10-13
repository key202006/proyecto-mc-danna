from flask import current_app
from Models.evaluacion import Evaluacion
import uuid


class evaluacionService:

    def show():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT EVA_ID, EVA_UUID, EVA_NOMBRE, EVA_CODIGO, EVA_PORCENTAJE, EVA_FECHA FROM T_EVALUACION")
        data = c.fetchall()
        c.close()
        return [ Evaluacion(x[0], x[1], x[2], x[3], x[4], x[5]) for x in data ]

    def add(data):
        nuevo_uuid = str(uuid.uuid4())  # genera un uuid
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_EVALUACION (EVA_UUID, EVA_NOMBRE, EVA_CODIGO, EVA_PORCENTAJE, EVA_FECHA)
                 VALUES (%s, %s, %s, %s, %s)"""  # consulta parametrizada
        c.execute(sql, (nuevo_uuid, data['EVA_NOMBRE'], data['EVA_CODIGO'], data['EVA_PORCENTAJE'], data['EVA_FECHA']))
        current_app.mysql.connection.commit()  # guarda los cambios
        id = c.lastrowid
        c.close()
        respuesta = {"EVA_ID": id, "EVA_UUID": nuevo_uuid}
        respuesta.update(data)
        return respuesta

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT EVA_ID FROM T_EVALUACION WHERE EVA_UUID = %s", [uuid])
        if c.fetchone() is None:
            c.close()
            return 404
        campos = ["EVA_NOMBRE", "EVA_CODIGO", "EVA_PORCENTAJE", "EVA_FECHA"]
        cambios = [ k for k in campos if k in data ]
        sql = "UPDATE T_EVALUACION SET " + ", ".join([ k + " = %s" for k in cambios ]) + " WHERE EVA_UUID = %s"
        c.execute(sql, [ data[k] for k in cambios ] + [uuid])
        current_app.mysql.connection.commit()
        c.close()
        return 200

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_EVALUACION WHERE EVA_UUID = %s", [uuid])
        current_app.mysql.connection.commit()
        if c.rowcount > 0:
            codigo = 200
        else:
            codigo = 404
        c.close()
        return codigo
