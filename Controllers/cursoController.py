from Services.cursoService import cursoService


class cursoController:

    def show():
        data = cursoService.show()
        return data
