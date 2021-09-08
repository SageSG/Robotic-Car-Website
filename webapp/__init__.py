from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
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

from webapp import routes

