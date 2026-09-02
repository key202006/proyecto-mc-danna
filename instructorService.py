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