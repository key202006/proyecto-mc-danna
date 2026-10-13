from flask import current_app
from Models.evaluacion import Evaluacion
import uuid

class evaluacionService:
    
    def add(data):
        uuid_eva = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        sql = """
            INSERT INTO T_EVALAUCION (EVA_UUID, EVA_NOMBRE, EVA_CODIGO, EVA_PORCENTAJE, EVA_FECHA) 
            VALUES (%s, %s, %s, %s, %s)"""
        c.execute(sql, (uuid_eva, data["nombre"], data["codigo"], data["porcentaje"], data["fecha"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_eva, "nombre": data["nombre"], "codigo": data["codigo"], "porcentaje": data["porcentaje"], "fecha": data["fecha"]}

    
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM T_EVALAUCION WHERE EVA_UUID = %s"
        c.execute(sql, [uuid])
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """
            UPDATE T_EVALAUCION 
            SET EVA_NOMBRE = %s, EVA_CODIGO = %s, EVA_PORCENTAJE = %s, EVA_FECHA = %s 
            WHERE EVA_UUID = %s"""
        c.execute(sql, (data["nombre"], data["codigo"], data["porcentaje"], data["fecha"], uuid))
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo


    def show():
        sql = "SELECT * FROM T_EVALAUCION"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [Evaluacion(x[0], x[1], x[2], x[3], x[4], x[5]).to_dict() for x in data]
        c.close()
        return data