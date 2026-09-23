# blueprint
from flask import Blueprint
from Controllers.instructorController import instructorController

ins_bp = Blueprint('ins_bp', __name__)

@ins_bp.route('/', methods=['GET'])
def home():
    return instructorController.show()

@ins_bp.route('/', methods=['POST'])
def add():
    return instructorController.add()

@ins_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return instructorController.delete(uuid)
