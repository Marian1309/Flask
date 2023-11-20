from flask import Blueprint

cookie = Blueprint("cookie", __name__, template_folder="templates")

from . import views
