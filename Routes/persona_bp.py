# blueprint  
from flask import Blueprint
from Controllers.personaController import personaController

per_bp = Blueprint('per_bp', __name__)

@per_bp.route('/', methods=['GET'])
def home():
    personaController.show()

@per_bp.route('/', methods=['POST'])
def add():
    return  personaController.add()

@per_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return personaController.delete(uuid)
