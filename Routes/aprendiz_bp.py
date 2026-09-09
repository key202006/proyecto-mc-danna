# blueprint  
from flask import Blueprint
from Controllers.aprendizController import aprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'])
def home():
    aprendizController.show()

@apr_bp.route('/', methods=['POST'])
def add():
    return  aprendizController.add()

@apr_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return aprendizController.delete(uuid)

