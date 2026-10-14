from flask import current_app
from Models.curso import Curso
import uuid

class cursoService:
    
    def add(data):
        uuid_cur = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        sql = """
            INSERT INTO T_CURSO (CUR_UUID, CUR_NOMBRE, CUR_CODIGO, CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION) 
            VALUES (%s, %s, %s, %s, %s, %s)"""
        c.execute(sql, (uuid_cur, data["nombre"], data["codigo"], data["duracion"], data["costo"], data["descripcion"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        return {"id": id, "uuid": uuid_cur, "nombre": data["nombre"], "codigo": data["codigo"], "duracion": data["duracion"], "costo": data["costo"], "descripcion": data["descripcion"]}

    
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM T_CURSO WHERE CUR_UUID = %s"
        c.execute(sql, [uuid])
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

   
    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """
            UPDATE T_CURSO 
            SET CUR_NOMBRE = %s, CUR_CODIGO = %s, CUR_DURACION = %s, CUR_COSTO = %s, CUR_DESCRIPCION = %s 
            WHERE CUR_UUID = %s"""
        c.execute(sql, (data["nombre"], data["codigo"], data["duracion"], data["costo"], data["descripcion"], uuid))
        c.connection.commit()
        codigo = 200 if c.rowcount > 0 else 404
        c.close()
        return codigo

    
    def show():
        sql = "SELECT * FROM T_CURSO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [Curso(x[0], x[1], x[2], x[3], x[4], x[5], x[6]).to_dict() for x in data]
        c.close()
        return data