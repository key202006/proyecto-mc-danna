
from flask import Blueprint
from Controllers.cursoController import cursoController

cur_bp = Blueprint('cur_bp', __name__)

@cur_bp.route('/', methods=['GET'])
def show():
    return cursoController.show()

@cur_bp.route('/', methods=['POST'])
def add():
    return cursoController.add()

@cur_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return cursoController.delete(uuid)

@cur_bp.route('/<uuid>', methods=['PATCH'])
def update(uuid):
    return cursoController.update(uuid)