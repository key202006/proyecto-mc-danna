from flask import current_app
from Models.instructor import Instructor
import uuid

class instructorService:
  
    def add(data):
        uuid_ins = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        sql = """
            INSERT INTO T_INSTRUCTOR (INS_UUID, INS_ESPECIALIDAD, INS_PER_ID) 
            VALUES (%s, %s, %s)"""
        c.execute(sql, (uuid_ins, data["especialidad"], data["per_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_ins, "especialidad": data["especialidad"], "per_id": data["per_id"]}

    
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM T_INSTRUCTOR WHERE INS_UUID = %s"
        c.execute(sql, [uuid])
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

    
    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """
            UPDATE T_INSTRUCTOR 
            SET INS_ESPECIALIDAD = %s, INS_PER_ID = %s 
            WHERE INS_UUID = %s"""
        c.execute(sql, (data["especialidad"], data["per_id"], uuid))
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

    
    def show():
        sql = "SELECT * FROM T_INSTRUCTOR"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [Instructor(x[0], x[1], x[2], x[3]).to_dict() for x in data]
        c.close()
        return data