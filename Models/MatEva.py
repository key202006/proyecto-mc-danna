class MatEva:
    def __init__(self, mate_id, mate_uuid, mate_nota, mate_eva_id ,mate_mat_id):
        self.__mate_id = mate_id
        self.__mate_uuid = mate_uuid
        self.__mate_nota = mate_nota
        self.__mate_eva_id = mate_eva_id
        self.__mate_mat_id = mate_mat_id
    
    def to_dict(self):
        return {
            'mate_id': self.__mate_id,
            'mate_uuid': self.__mate_uuid,
            'mate_nota': self.__mate_nota,
            'mate_eva_id': self.__mate_eva_id,
            'mate_mat_id': self.__mate_mat_id 
        } 