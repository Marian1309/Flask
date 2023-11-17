from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = b"Powerful secret"
app.config['SECRET_KEY'] = 'Powerful secret'
csrf = CSRFProtect(app)

from app import views
