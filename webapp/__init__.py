import os
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
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USER_TLS"] = True
app.config["MAIL_USER_SSL"] = False
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USER")
app.config["MAIL_PASS"] = os.environ.get("MAIL_PASSWORD")

mail = Mail(app)

from webapp import routes

