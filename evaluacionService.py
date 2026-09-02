from flask import current_app
from Model.matricula import Evaluacion
def show():
    sql = "SELECT * FROM T_EVALUACION"
    c = current_app.mysql.connection.cursor()
    c.execute(sql)
    data = c.fetchall()
    data = [ Evaluacion(x[0], x[1], x[2])for x in data]
    print(data)
    return data