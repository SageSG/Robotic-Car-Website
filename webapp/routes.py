from flask import Flask, render_template, url_for, redirect, flash, request
from webapp import app, db, bcrypt, mail
from webapp.forms import RegistratationForm, LoginForm, ForgotForm, ResetForm
from webapp.models import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

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
                next_page = request.args.get('next') # Allow user to be directed to requested page (if available) upon authorised login
                return redirect(next_page) if next_page else redirect(url_for("home"))

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

# Function to send email using flask-mail
def send_mail(user):
    key = user.get_reset_key()
    content = Message("Password Reset Request", sender="jacktan210718@gmail.com", recipients=[user.email])
    content.body = f'''Reset password: {url_for('reset', key=key, _external=True)}'''
    mail.send(content)

@app.route("/forgot", methods=["GET", "POST"])
def forgot():
    form = ForgotForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_mail(user)
        send_mail(user)
        flash(f"Your password reset request has been sent to the specified email.", "success")

    return render_template("forgot.html", title="Forgot Password", form=form)

@app.route("/reset/<key>", methods=["GET", "POST"])
def reset(key):
    user_id = User.verify_reset_key(key)
    if user_id is None:
        flash("Invalid request link.", "warning")
        return redirect(url_for("forgot"))
    else:
        form = ResetForm()
        if form.validate_on_submit():
            # Hash the password variable
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

            # Store user details into database
            user_id.password = hashed_password
            db.session.commit()
        return render_template('reset.html', title="Reset Password", form=form)

# Authorised Pages

# Logout function
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

# Account
@app.route("/account")
@login_required     #Only logged in users can access this page
def account():
    return render_template("account.html", title="Account")