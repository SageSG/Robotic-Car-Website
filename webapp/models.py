from webapp import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# Reload user from the user id stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create User database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(60),nullable=False)
    reset_key = db.Column(db.String(60), nullable=True)

    # Generate a reset token for resetting of password
    def get_reset_key(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_key(key):
        s = Serializer(app.config["SECRET_KEY"])
        try:
            # Try to retrieve the user_id from the key
            user_id = s.loads(key)['user_id']
        except:
            return None
        return User.query.get(user_id)


def __repr__(self):
    return f"User('{self.username}','{self.email}')"