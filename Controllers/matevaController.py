from Services.matEvaService import matEvaService


class matEvaController:

    def show():
        data = matEvaService.show()
        return data
