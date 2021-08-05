from flask import Flask
from flask_login import LoginManager, login_manager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RTRITHFGJNFJGFGHFJVNFJVVNVNJ'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#login_manager.login_message_category = 'info'

from app import views