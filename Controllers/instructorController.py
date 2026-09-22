from Services.instructorService import instructorService


class instructorController:

    def show():
        data = instructorService.show()
        return data
