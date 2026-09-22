from Services.imparteService import imparteService


class imparteController:

    def show():
        data = imparteService.show()
        return data
