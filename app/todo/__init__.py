from flask import Blueprint

todo_br = Blueprint("todo_br", __name__, template_folder="templates")

from . import views
