from Services.personaService import personaService


class personaController:

    def show():
        data = personaService.show()
        return data
