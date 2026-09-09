# blueprint  
from flask import Blueprint
from Controllers.Mat_evaController import Mat_evaController

mate_bp = Blueprint('mate_bp', __name__)

@mate_bp.route('/', methods=['GET'])
def home():
    mat_evaController.show()

@mate_bp.route('/', methods=['POST'])
def add():
    return  mat_evaController.add()

@mate_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return mat_evaController.delete(uuid)
