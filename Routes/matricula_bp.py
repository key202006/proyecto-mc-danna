# blueprint
from flask import Blueprint
from Controllers.matriculaController import matriculaController

mat_bp = Blueprint('mat_bp', __name__)

@mat_bp.route('/', methods=['GET'])
def home():
    return matriculaController.show()

@mat_bp.route('/', methods=['POST'])
def add():
    return matriculaController.add()
    
@mat_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return matriculaController.delete(uuid)
