from flask import current_app
from Models.matricula import Matricula
import uuid

class matriculaService:
    
    def add(data):
        uuid_mat = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        sql = """
            INSERT INTO T_MATRICULA (MAT_UUID, MAT_ESTADO, MAT_FECHA_INSCRIPCION, MAT_APR_ID, MAT_CUR_ID) 
            VALUES (%s, %s, %s, %s, %s)"""
        c.execute(sql, (uuid_mat, data["estado"], data["fecha_inscripcion"], data["apr_id"], data["cur_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_mat, "estado": data["estado"], "fecha_inscripcion": data["fecha_inscripcion"], "apr_id": data["apr_id"], "cur_id": data["cur_id"]}

   
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM T_MATRICULA WHERE MAT_UUID = %s"
        c.execute(sql, [uuid])
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

  
    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """
            UPDATE T_MATRICULA 
            SET MAT_ESTADO = %s, MAT_FECHA_INSCRIPCION = %s, MAT_APR_ID = %s, MAT_CUR_ID = %s 
            WHERE MAT_UUID = %s"""
        c.execute(sql, (data["estado"], data["fecha_inscripcion"], data["apr_id"], data["cur_id"], uuid))
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

    
    def show():
        sql = "SELECT * FROM T_MATRICULA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [Matricula(x[0], x[1], x[2], x[3], x[4], x[5]).to_dict() for x in data]
        c.close()
        return data