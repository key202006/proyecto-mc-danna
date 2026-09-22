from Services.evaluacionService import evaluacionService


class evaluacionController:

    def show():
        data = evaluacionService.show()
        return data
