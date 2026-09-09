from flask import current_app
from Model.matricula import Instructor

def show():
    sql = "SELECT * FROM T_INSTRUCTOR"
    c = current_app.mysql.connection.cursor()
    c.execute(sql)
    data = c.fetchall()
    data = [ Instructor(x[0], x[1], x[2])for x in data]
    c.close()
    return data


def delete(uuid):
        c = current_app.mysql.connection.cursor()
        sql = """
            DELETE FROM T_INSTRUCTOR WHERE APR_UUID = %s"""
        c.execute(sql,[ uuid ])
        c.connection.commit()
        if c.rowcount > 0 :
             codigo = 200
        else:
             codigp = 404


        c.close()
        return codigo
