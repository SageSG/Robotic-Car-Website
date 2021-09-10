from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_mail import Mail

app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Set secret key to prevent modification of cookies and CSRF attacks
app.config['SECRET_KEY'] = '3f0d3ca61975ec2ca4b764d10da99b82'

# Password hashing
bcrypt = Bcrypt(app)

# Helps to handle the sessions
login_manager = LoginManager(app)

# Users who try to access page that requires authentication will be redirected to login
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Configurations for mail
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config["MAIL_USERNAME"] = "jacktan210718@gmail.com"
app.config["MAIL_PASS"] = "#4LOATI40oMOvfuAGXz^6P4e*"
mail = Mail(app)

from webapp import routes

