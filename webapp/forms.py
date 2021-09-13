from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models.users import User

# Create registration form for the webapp
class RegistratationForm(FlaskForm):

    # Required form field called username that must be between 2 to 20 chars long
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])

    # Required form field called email
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    # Check if username and email exists in the database
    # Use generalised error message for security purposes
    # Functions must start with validate_*
    # - In the background, Flask is checking for
    #   functions with the pattern validate_* and calling them

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Invalid username.")

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError("Invalid email address.")

# Login form
class LoginForm(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# Used to send password change request
class ForgotForm(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Reset Password")

# Used to reset user's password
class ResetForm(FlaskForm):
    new_password = PasswordField("New Password", validators=[DataRequired()])
    confirm_new_passwd = PasswordField("Confirm New Password", validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField("Change Password")

