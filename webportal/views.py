from flask import Blueprint
from flask import Flask, render_template

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


@views.route("/robots.txt")
def robots():
    return render_template('robots.txt', title="Robots")


@views.route("/send_command")
def send_command():
    pass


@views.route("/retrieve_stats")
def retrieve_stats():
    pass
