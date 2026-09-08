# blueprint
from flask import Blueprint
from Controllers.EvaluacionController import EvaluacionController

eva_bp = Blueprint('eva_bp', __name__)

@eva_bp.route('/', methods=['GET'])
def home():
    return EvaluacionController.show()

@eva_bp.route('/', methods=['POST'])
def add():
    return EvaluacionController.add()