from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_webportal():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '3f0d3ca61975ec2ca4b764d10da99b82'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    db = SQLAlchemy(app)
    db.create_all()
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app