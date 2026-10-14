class Evaluacion:
    def __init__(self, eva_id, eva_uuid, eva_nombre, eva_codigo , eva_porcentaje, eva_fecha):
        self.__eva_id = eva_id
        self.__eva_uuid = eva_uuid
        self.__eva_nombre = eva_nombre
        self.__eva_codigo = eva_codigo
        self.__eva_porcentaje = eva_porcentaje
        self.__eva_fecha = eva_fecha  

    def to_dict(self):
        return {
            'eva_id': self.__eva_id,
            'eva_uuid': self.__eva_uuid,
            'eva_nombre': self.__eva_nombre,
            'eva_codigo': self.__eva_codigo,
            'eva_porcentaje': self.__eva_porcentaje,
            'eva_fecha': self.__eva_fecha 
        }