from flask import current_app
from Models.Aprendiz import Aprendiz
import uuid

class aprendizService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_apr = uuid.uuid4() # genera un uuid
        c  = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_APRENDIZ (APR_UUID, APR_FECHA_NAC, APR_PER_ID) VALUES  
        (%s, %s, %s)""" #consulta parametrizada
        c.execute(sql, (uuid_apr, data['APR_FECHA_NAC'], data['APR_PER_ID']))
        c.connection.commit() # guarda los cambios
        id = c.lastrowid # devuelve el id del ultimo registro insertado
        c.close()
        respuesta = {"id":id, "APR_UUID": uuid_apr, "APR_FECHA_NAC" : data["APR_FECHA_NAC"], 
                     "APR_PER_ID" : data["APR_PER_ID"]}
        return respuesta

    def delete(uuid):
        c  = current_app.mysql.connection.cursor()
        sql = f""" delete from T_APRENDIZ where APR_UUID = %s"""
        c.execute(sql, [uuid])
        c.connection.commit() # guarda los cambios
        if c.rowcount > 0 :
           codigo= 200 
        else:
           codigo = 404
            
        c.close()
        return codigo

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_APRENDIZ"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [ Aprendiz(x[0], x[1], x[2], x[3]) for x in data]
        c.close()
        return data
# relacionado todo lo q esta en la base de datos con la clase aprendiz
