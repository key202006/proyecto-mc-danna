from flask import current_app
from Models.persona import Persona
import uuid

class personaService:
    def add(data):
        uuid_per = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        sql = """
            INSERT INTO T_PERSONA (PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOCUMENTO) 
            VALUES (%s, %s, %s, %s, %s, %s)"""
        c.execute(sql, (uuid_per, data["pri_nombre"], data["seg_nombre"], data["pri_apellido"], data["seg_apellido"], data["documento"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_per, "pri_nombre": data["pri_nombre"], "seg_nombre": data["seg_nombre"], "pri_apellido": data["pri_apellido"], "seg_apellido": data["seg_apellido"], "documento": data["documento"]}

     
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM T_PERSONA WHERE PER_UUID = %s"
        c.execute(sql, [uuid])
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

   
    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """
            UPDATE T_PERSONA 
            SET PER_PRI_NOMBRE = %s, PER_SEG_NOMBRE = %s, PER_PRI_APELLIDO = %s, PER_SEG_APELLIDO = %s, PER_DOCUMENTO = %s 
            WHERE PER_UUID = %s"""
        c.execute(sql, (data["pri_nombre"], data["seg_nombre"], data["pri_apellido"], data["seg_apellido"], data["documento"], uuid))
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

    
    def show():
        sql = "SELECT * FROM T_PERSONA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [Persona(x[0], x[1], x[2], x[3], x[4], x[5], x[6]).to_dict() for x in data]
        c.close()
        return data

    def obtener_id(id):
        sql = "SELECT * FROM T_PERSONA WHERE PER_ID = %s"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql,(id,))
        data = c.fetchone()
        if data is None:
            return "No se encontro la persona "
        id_per = Persona(data[0])
        c.close()
        return id_per