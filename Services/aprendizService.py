from flask import current_app
from Models.aprendiz import Aprendiz
import uuid

class aprendizService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_apr = uuid.uuid4()
        c  = current_app.mysql.connection.cursor()
        sql = """
            INSERT INTO T_APRENDIZ ( APR_UUID, APR_FECHA_NAC, APR_PER_ID) 
            VALUES (%s, %s, %s)"""
        c.execute(sql, ( uuid_apr, data["fecha_nac"],
                         data["per_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id":id, "uuid": uuid_apr,
                        "fecha_nac": data["fecha_nac"],
                        "per_id":data["per_id"]}
        return respuesta

    def delete(uuid):
        c  = current_app.mysql.connection.cursor()
        sql = """   
            DELETE FROM T_APRENDIZ WHERE APR_UUID = %s"""
        c.execute(sql,[ uuid ])
        c.connection.commit()
        if c.rowcount > 0 :            
             codigo = 200
        else:         
             codigo = 404

        c.close()
        return codigo

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """ 
            UPDATE T_APRENDIZ 
            SET APR_FECHA_NAC = %s, APR_PER_ID = %s 
            WHERE APR_UUID = %s"""
        c.execute(sql, (data["fecha_nac"], data["per_id"], uuid))
        c.connection.commit()
        if c.rowcount > 0:
            codigo = 200
        else:
            codigo = 404

        c.close()
        return codigo

    def show():
        sql = "SELECT * FROM T_APRENDIZ"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        data = [  Aprendiz(x[0],x[1],x[2],x[3]).to_dict() for x in data ]
        c.close()
        return data
