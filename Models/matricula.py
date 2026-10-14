class Matricula:
    def __init__(self, mat_id, mat_uuid, mat_estado, mat_fecha_inscripcion ,mat_apr_id , mat_cur_id):
        self.__mat_id = mat_id
        self.__mat_uuid = mat_uuid
        self.__mat_estado = mat_estado
        self.__mat_fecha_inscripcion = mat_fecha_inscripcion
        self.__mat_apr_id = mat_apr_id
        self.__mat_cur_id = mat_cur_id
    
    def to_dict(self):
        return {
            'mat_id':       self.__mat_id,
            'mat_uuid':     self.__mat_uuid,
            'mat_estado':   self.__mat_estado,
            'mat_fecha_inscripcion':   self.__mat_fecha_inscripcion,
            'mat_apr_id':   self.__mat_apr_id,
            'mat_cur_id':   self.__mat_cur_id
        } 