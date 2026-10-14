class Imparte:
    def __init__(self, imp_id, imp_uuid, imp_rol, imp_fecha_asignacion, imp_cur_id , imp_ins_id):
        self.__imp_id = imp_id
        self.__imp_uuid = imp_uuid
        self.__imp_rol = imp_rol
        self.__imp_fecha_asignacion = imp_fecha_asignacion
        self.__imp_cur_id = imp_cur_id
        self.__imp_ins_id = imp_ins_id  

    def to_dict(self):
        return {
            'imp_id': self.__imp_id,
            'imp_uuid': self.__imp_uuid,
            'imp_rol': self.__imp_rol,
            'imp_fecha_asignacion': self.__imp_fecha_asignacion,
            'imp_cur_id': self.__imp_cur_id,
            'imp_ins_id': self.__imp_ins_id
        }