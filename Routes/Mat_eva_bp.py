# blueprint  
from flask import Blueprint
from Controllers.matevaController import matEvaController

mate_bp = Blueprint('mate_bp', __name__)

@mate_bp.route('/', methods=['GET'])
def home():
    matEvaController.show()

@mate_bp.route('/', methods=['POST'])
def add():
    return  matEvaController.add()

@mate_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return matEvaController.delete(uuid)
