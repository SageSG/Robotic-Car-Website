from flask import Flask, render_template, url_for, redirect, flash
from webapp import app, db, bcrypt
from webapp.forms import RegistratationForm, LoginForm
from webapp.models import User
from flask_login import login_user, current_user, logout_user

# @app.route specifies the URL
# render_template(<html file>)
# - retrieves the html file from templates folder and use it for the web app,
# - able to pass in parameters that can be used in the HTML files using code blocks {%%}, {{}}
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home Page")

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Redirect authenticated user to home page
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm() #Specify form to be used on the page

    # Check if signed in successfully
    if form.validate_on_submit():
        # Check if email address exists
        email = User.query.filter_by(email=form.email.data).first()
        if email:   # Email exists
            # Check if password is correct
            hashed_password = email.password
            check = bcrypt.check_password_hash(hashed_password, form.password.data)
            if check:
                login_user(email, remember=form.remember.data)
                return redirect(url_for("home"))

        #Email does not exists or incorrect password
        flash("Invalid login credentials. Login unsuccessful.", "danger")

    return render_template('login.html', title="Login", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():

    # Redirect authenticated user to home page
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = RegistratationForm() #Specify form to be used on the page
    # Check if form is submitted successfully
    if form.validate_on_submit():
        # Hash the password variable
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

        # Store user details into database
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Account {form.username.data} has been successfully created!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title="Register", form=form)

@app.route("/reset")
def reset():
    return render_template('reset.html', title="Reset Password")

# Logout function
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))