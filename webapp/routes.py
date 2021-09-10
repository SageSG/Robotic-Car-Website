from flask import Flask, render_template, url_for, redirect, flash, request
from webapp import app, db, bcrypt, mail
from webapp.forms import RegistratationForm, LoginForm, ForgotForm, ResetForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from flask import Flask, render_template, url_for, redirect, flash
from webapp import app, db, bcrypt
from webapp.forms import RegistratationForm, LoginForm
from flask_login import login_user, current_user, logout_user
from flask import jsonify
from webapp.models import User

# For sending email
from webapp.google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# @app.route specifies the URL
# render_template(<html file>)
# - retrieves the html file from templates folder and use it for the web app,
# - able to pass in parameters that can be used in the HTML files using code blocks {%%}, {{}}
@app.route("/")

# Home page
@app.route("/home")
def home():
    return render_template('home.html', title="Home Page")

# About page
@app.route("/about")
def about():
    return render_template('about.html', title="About")

# Login page
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

# Register page
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

# Function to send email using Gmail API
def send_gmail(user):

    key = user.get_reset_key()  #Generate a valid key for user with specified email

    # Store the key into the database
    user.reset_key = key
    db.session.commit()

    CLIENT_SECRET_FILE = 'credentials.json' # Contains the Client ID and Client Secret
    API_NAME = 'gmail'  # Name of the API used
    API_VERSION = 'v1'  # API version
    SCOPES = ['https://mail.google.com/']   #endpoint that can be accessed by the webapp

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES) # Create the API service

    emailMsg = f'''To reset your password click here: {url_for('reset', key=key, _external=True)}'''
    emailMsg += f'''\n\nIf you did not request this, please ignore this message.'''
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = user.email
    mimeMessage['subject'] = 'Password Reset'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    # Send the email using the GMAIL API service
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

# Request to reset password page
@app.route("/forgot", methods=["GET", "POST"])
def forgot():

    form = ForgotForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # Check if user exists
        if user is not None:
            send_gmail(user)
        else:
            pass

        flash(f"If the email exists, the password reset request has been sent to the specified email.", "success")

    return render_template("forgot.html", title="Forgot Password", form=form)

# Reset password page
@app.route("/reset/<key>", methods=["GET", "POST"])
def reset(key):

    user = User.verify_reset_key(key)

    if user is not None and user.reset_key == key:
        form = ResetForm()
        if form.validate_on_submit():
            # Hash the password variable
            hashed_password = bcrypt.generate_password_hash(form.confirm_new_passwd.data).decode("utf-8")

            # Store user details into database
            user.password = hashed_password

            # Generate a new key and store to DB to ensure that user cannot use the same link to reset again
            user.reset_key = user.get_reset_key()
            db.session.commit()

            flash("Please login again.", "danger")
            return redirect(url_for("login"))
    else:
        flash("Invalid request link.", "warning")
        return redirect(url_for("forgot"))


    return render_template('reset.html', title="Reset Password", form=form)

# robots.txt page
@app.route("/robots.txt")
def robots():
    return render_template('robots.txt', title="Robots")

# Authorised Pages

# Logout page
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

# Account
@app.route("/account", methods=["GET", "POST"])
@login_required     #Only logged in users can access this page
def account():
    form = ResetForm()
    if form.validate_on_submit():
        # Hash the password variable
        hashed_password = bcrypt.generate_password_hash(form.confirm_new_passwd.data).decode("utf-8")

        # Store user details into database
        current_user.password = hashed_password

        db.session.commit()

        # Logout the user after password has been changed
        logout_user()

        return redirect(url_for("login"), )

    return render_template("account.html", title="Account", form=form)