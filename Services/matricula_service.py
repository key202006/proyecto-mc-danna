from flask import current_app
from Models.Matricula import Aprendiz

class aprendizService:
   

    def show():
        sql = "SELECT * FROM T_APRENDIZ"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        # c.close()
        return ""