# blueprint
from flask import Blueprint
from Controllers.InstructorController import InstructorController

ins_bp = Blueprint('ins_bp', __name__)

@ins_bp.route('/', methods=['GET'])
def home():
    return InstructorController.show()

@ins_bp.route('/', methods=['POST'])
def add():
    return "agregar Instructor"
