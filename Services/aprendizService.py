from flask import current_app
from Models.Aprendiz import Aprendiz
import uuid


class aprendizService:

    def show():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT APR_ID, APR_UUID, APR_FECHA_NAC, APR_PER_ID FROM T_APRENDIZ")
        data = c.fetchall()
        c.close()
        return [ Aprendiz(x[0], x[1], x[2], x[3]) for x in data ]

    def add(data):
        nuevo_uuid = str(uuid.uuid4())  # genera un uuid
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_APRENDIZ (APR_UUID, APR_FECHA_NAC, APR_PER_ID)
                 VALUES (%s, %s, %s)"""  # consulta parametrizada
        c.execute(sql, (nuevo_uuid, data['APR_FECHA_NAC'], data['APR_PER_ID']))
        current_app.mysql.connection.commit()  # guarda los cambios
        id = c.lastrowid
        c.close()
        respuesta = {"APR_ID": id, "APR_UUID": nuevo_uuid}
        respuesta.update(data)
        return respuesta

    def update(uuid, data):
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT APR_ID FROM T_APRENDIZ WHERE APR_UUID = %s", [uuid])
        if c.fetchone() is None:
            c.close()
            return 404
        campos = ["APR_FECHA_NAC", "APR_PER_ID"]
        cambios = [ k for k in campos if k in data ]
        sql = "UPDATE T_APRENDIZ SET " + ", ".join([ k + " = %s" for k in cambios ]) + " WHERE APR_UUID = %s"
        c.execute(sql, [ data[k] for k in cambios ] + [uuid])
        current_app.mysql.connection.commit()
        c.close()
        return 200

    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_APRENDIZ WHERE APR_UUID = %s", [uuid])
        current_app.mysql.connection.commit()
        if c.rowcount > 0:
            codigo = 200
        else:
            codigo = 404
        c.close()
        return codigo

    def get_boletin(uuid):
        # busca al aprendiz con los datos de su persona
        c = current_app.mysql.connection.cursor()
        c.execute("""SELECT A.APR_ID, A.APR_UUID, A.APR_FECHA_NAC, P.PER_PRI_NOMBRE, P.PER_SEG_NOMBRE,
                            P.PER_PRI_APELLIDO, P.PER_SEG_APELLIDO, P.PER_DOCUMENTO
                     FROM T_APRENDIZ A JOIN T_PERSONA P ON P.PER_ID = A.APR_PER_ID
                     WHERE A.APR_UUID = %s""", [uuid])
        a = c.fetchone()
        if a is None:
            c.close()
            return None
        aprendiz = {"APR_UUID": a[1], "APR_FECHA_NAC": a[2],
                    "PER_PRI_NOMBRE": a[3], "PER_SEG_NOMBRE": a[4],
                    "PER_PRI_APELLIDO": a[5], "PER_SEG_APELLIDO": a[6],
                    "PER_DOCUMENTO": a[7], "matriculas": []}

        # sus matriculas con el nombre del curso
        c.execute("""SELECT M.MAT_ID, M.MAT_UUID, M.MAT_ESTADO, C.CUR_NOMBRE
                     FROM T_MATRICULA M JOIN T_CURSO C ON C.CUR_ID = M.MAT_CUR_ID
                     WHERE M.MAT_APR_ID = %s""", [a[0]])
        for m in c.fetchall():
            matricula = {"MAT_UUID": m[1], "MAT_ESTADO": m[2], "CUR_NOMBRE": m[3], "notas": []}

            # las notas de cada matricula (tabla T_MAT_EVA) con su evaluacion
            c.execute("""SELECT E.EVA_NOMBRE, E.EVA_PORCENTAJE, N.MATE_UUID, N.MATE_NOTA
                         FROM T_MAT_EVA N JOIN T_EVALUACION E ON E.EVA_ID = N.MATE_EVA_ID
                         WHERE N.MATE_MAT_ID = %s""", [m[0]])
            suma = 0
            porcentajes = 0
            for n in c.fetchall():
                matricula["notas"].append({"EVA_NOMBRE": n[0], "EVA_PORCENTAJE": n[1],
                                           "MATE_UUID": n[2], "MATE_NOTA": n[3]})
                suma = suma + float(n[3]) * float(n[1])
                porcentajes = porcentajes + float(n[1])
            # promedio ponderado por el porcentaje de cada evaluacion
            if porcentajes > 0:
                matricula["PROMEDIO"] = round(suma / porcentajes, 2)
            else:
                matricula["PROMEDIO"] = None
            aprendiz["matriculas"].append(matricula)
        c.close()
        return aprendiz
