class Curso:
    def __init__(self, cur_id, cur_uuid, cur_nombre, cur_codigo , cur_duracion ,cur_costo ,cur_descripcion):
        self.__cur_id = cur_id
        self.__cur_uuid = cur_uuid
        self.__cur_nombre = cur_nombre
        self.__cur_codigo = cur_codigo
        self.__cur_duracion = cur_duracion
        self.__cur_costo = cur_costo
        self.__cur_descripcion = cur_descripcion

    def to_dict(self):
        return {
            'cur_id': self.__cur_id,
            'cur_uuid': self.__cur_uuid,
            'cur_nombre': self.__cur_nombre,
            'cur_codigo': self.__cur_codigo,
            'cur_duracion': self.__cur_duracion,
            'cur_costo': self.__cur_costo,
            'cur_descripcion': self.__cur_descripcion
        }