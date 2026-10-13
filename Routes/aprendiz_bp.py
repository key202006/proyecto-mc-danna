# blueprint  
from flask import Blueprint
from Controllers.aprendizController import aprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'])
def home():
    return aprendizController.show()

@apr_bp.route('/', methods=['POST'])
def add():
    return  aprendizController.add()

@apr_bp.route('/<uuid>', methods=['GET'])
def get_one(uuid):
    return aprendizController.get_one(uuid)

@apr_bp.route('/<uuid>', methods=['PUT'])
def update(uuid):
    return aprendizController.update(uuid)

@apr_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return aprendizController.delete(uuid)

