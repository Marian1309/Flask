from flask import Blueprint

feedback_br = Blueprint("feedback_br", __name__, template_folder="templates")

from . import views
