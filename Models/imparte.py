<<<<<<< HEAD
class Imparte:

    def __init__(self, IMP_ID, IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID):
        self.__IMP_ID               = IMP_ID
        self.__IMP_UUID             = IMP_UUID
        self.__IMP_ROL              = IMP_ROL
        self.__IMP_FECHA_ASIGNACION = IMP_FECHA_ASIGNACION
        self.__IMP_CUR_ID           = IMP_CUR_ID
        self.__IMP_INS_ID           = IMP_INS_ID

    def to_dict(self):
        return {
            "IMP_ID": self.__IMP_ID,
            "IMP_UUID": self.__IMP_UUID,
            "IMP_ROL": self.__IMP_ROL,
            "IMP_FECHA_ASIGNACION": self.__IMP_FECHA_ASIGNACION,
            "IMP_CUR_ID": self.__IMP_CUR_ID,
            "IMP_INS_ID": self.__IMP_INS_ID
=======
class Imparte:

    def __init__(self, IMP_ID, IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID):
        self.__IMP_ID               = IMP_ID
        self.__IMP_UUID             = IMP_UUID
        self.__IMP_ROL              = IMP_ROL
        self.__IMP_FECHA_ASIGNACION = IMP_FECHA_ASIGNACION
        self.__IMP_CUR_ID           = IMP_CUR_ID
        self.__IMP_INS_ID           = IMP_INS_ID

    def to_dict(self):
        return {
            "IMP_ID": self.__IMP_ID,
            "IMP_UUID": self.__IMP_UUID,
            "IMP_ROL": self.__IMP_ROL,
            "IMP_FECHA_ASIGNACION": self.__IMP_FECHA_ASIGNACION,
            "IMP_CUR_ID": self.__IMP_CUR_ID,
            "IMP_INS_ID": self.__IMP_INS_ID
>>>>>>> acba4aaa736908a298e0dbf244d55e209f3b8047
        }