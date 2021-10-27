from flask import Blueprint
from flask import Flask, render_template
from webportal.models.carstats import get_stats

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', title="Home Page")


@views.route("/about")
def about():
    return render_template('about.html', title="About")


@views.route("/terminal")
def control():
    return render_template('terminal.html', title="Terminal")


@views.route("/dashboard")
def dashboard():
    data = get_stats()
    return render_template('dashboard.html', title="Dashboard", data=data)


@views.route("/robots.txt")
def robots():
    return render_template('robots.txt', title="Robots")
