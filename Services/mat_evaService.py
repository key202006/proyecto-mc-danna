from flask import current_app
from Models.matEva import MatEva
import uuid

class mat_evaService:
 
    def add(data):
        uuid_mate = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        sql = """
            INSERT INTO T_MAT_EVA (MATE_UUID, MATE_NOTA, MATE_EVA_ID, MATE_MAT_ID) 
            VALUES (%s, %s, %s, %s)"""
        c.execute(sql, (uuid_mate, data["nota"], data["eva_id"], data["mat_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_mate, "nota": data["nota"], "eva_id": data["eva_id"], "mat_id": data["mat_id"]}

    
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM T_MAT_EVA WHERE MATE_UUID = %s"
        c.execute(sql, [uuid])
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """
            UPDATE T_MAT_EVA 
            SET MATE_NOTA = %s, MATE_EVA_ID = %s, MATE_MAT_ID = %s 
            WHERE MATE_UUID = %s"""
        c.execute(sql, (data["nota"], data["eva_id"], data["mat_id"], uuid))
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

  
    def show():
        sql = "SELECT * FROM T_MAT_EVA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [MatEva(x[0], x[1], x[2], x[3], x[4]).to_dict() for x in data]
        c.close()
        return data