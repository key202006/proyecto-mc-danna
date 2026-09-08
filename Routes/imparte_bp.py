# blueprint
from flask import Blueprint
from Controllers.ImparteController import ImparteController

imp_bp = Blueprint('imp_bp', __name__)

@imp_bp.route('/', methods=['GET'])
def home():
    return ImparteController.show()

@imp_bp.route('/', methods=['POST'])
def add():
    return ImparteController.add()