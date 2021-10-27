from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
DB_NAME = "database.db"
from webportal.models.carstats import CarStats
from webportal.controller.statscontroller import CarStatsControllerAPI
from webportal.controller.controlscontroller import ControlsControllerAPI


def create_webportal():
    app.config['SECRET_KEY'] = '3f0d3ca61975ec2ca4b764d10da99b82'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app



# API (To be seperated into another file)
api.add_resource(CarStatsControllerAPI, '/car/stats')
api.add_resource(ControlsControllerAPI, '/car/commands')