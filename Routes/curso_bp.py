# blueprint
from flask import Blueprint
from Controllers.CursoController import CursoController

cur_bp = Blueprint('cur_bp', __name__)


@cur_bp.route('/', methods=['GET'])
def home():
    return CursoController.show()

@cur_bp.route('/', methods=['POST'])
def add():
    return "agregar curso"
