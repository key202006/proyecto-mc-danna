# blueprint
from flask import Blueprint
from Controllers.imparteContoller import imparteController

imp_bp = Blueprint('imp_bp', __name__)

@imp_bp.route('/', methods=['GET'])
def home():
    return imparteController.show()

@imp_bp.route('/', methods=['POST'])
def add():
    return  imparteController.add()

@imp_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return imparteController.delete(uuid)
