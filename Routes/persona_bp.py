# blueprint  
from flask import Blueprint
from Controllers.PersonaController import PersonaController

per_bp = Blueprint('per_bp', __name__)

@per_bp.route('/', methods=['GET'])
def show():
    return PersonaController.show()

@per_bp.route('/', methods=['POST'])
def add():
    return PersonaController.add()

@per_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return PersonaController.delete(uuid)

@per_bp.route('/<uuid>', methods=['PATCH'])
def update(uuid):
    return PersonaController.update(uuid)

@per_bp.route('/<int:id>', methods=['GET'])
def obtener_id(id):
    return PersonaController.obtener_id(id)