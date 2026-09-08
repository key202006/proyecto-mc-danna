# blueprint  
from flask import Blueprint
from Controllers.PersonaController import PersonaController

per_bp = Blueprint('per_bp', __name__)

@per_bp.route('/', methods=['GET'])
def home():
    PersonaController.show()

@per_bp.route('/', methods=['POST'])
def add():
    return "agregar persona"