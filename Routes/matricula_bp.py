# blueprint
from flask import Blueprint
from Controllers.MatriculaController import MatriculaController

mat_bp = Blueprint('mat_bp', __name__)

@mat_bp.route('/', methods=['GET'])
def home():
    return MatriculaController.show()

@mat_bp.route('/', methods=['POST'])
def add():
    return "agregar matricula"
