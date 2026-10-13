from flask import current_app
from Models.imparte import Imparte
import uuid

class imparteService:
    
    def add(data):
        uuid_imp = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        sql = """
            INSERT INTO T_IMPARTE (IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID) 
            VALUES (%s, %s, %s, %s, %s)"""
        c.execute(sql, (uuid_imp, data["rol"], data["fecha_asignacion"], data["cur_id"], data["ins_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_imp, "rol": data["rol"], "fecha_asignacion": data["fecha_asignacion"], "cur_id": data["cur_id"], "ins_id": data["ins_id"]}

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM T_IMPARTE WHERE IMP_UUID = %s"
        c.execute(sql, [uuid])
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

 
    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """
            UPDATE T_IMPARTE 
            SET IMP_ROL = %s, IMP_FECHA_ASIGNACION = %s, IMP_CUR_ID = %s, IMP_INS_ID = %s 
            WHERE IMP_UUID = %s"""
        c.execute(sql, (data["rol"], data["fecha_asignacion"], data["cur_id"], data["ins_id"], uuid))
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo


    def show():
        sql = "SELECT * FROM T_IMPARTE"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [Imparte(x[0], x[1], x[2], x[3], x[4], x[5]).to_dict() for x in data]
        c.close()
        return data