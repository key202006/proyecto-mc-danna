from flask import current_app
from Model.persona import persona

def show():
    sql = "SELECT * FROM T_MAT_EVA"
    c = current_app.mysql.connection.cursor()
    c.execute(sql)
    data = c.fetchall()
    data = [ persona(x[0], x[1], x[2])for x in data]
    c.close()
    return data