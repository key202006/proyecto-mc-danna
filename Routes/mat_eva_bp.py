# blueprint  
from flask import Blueprint
from Controllers.mat_evaController import matEvaController

mateva_bp = Blueprint('mateva_bp', __name__)

@mateva_bp.route('/', methods=['GET'])
def home():
    return matEvaController.show()
    

@mateva_bp.route('/', methods=['POST'])
def add():
    return  matEvaController.add()

@mateva_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return matEvaController.delete(uuid)
