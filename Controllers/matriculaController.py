from Services.matriculaService import matriculaService


class matriculaController:

    def show():
        data = matriculaService.show()
        return data
