# Imports

from werkzeug import generate_password_hash, check_password_hash

from flask_login import UserMixin

from ...util import utils
from ...lib.database import db

class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(64), default=None)
    last_name = db.Column(db.String(64), default=None)
    age = db.Column(db.Integer, default=0)

    def __init__(self, user_obj):
        self.email = user_obj['email']
        self.password = generate_password_hash(user_obj['password'])
        self.first_name = user_obj['first_name']
        self.last_name = user_obj['last_name']
        self.age = int(user_obj['age'])

    def is_password_valid(self, _password):
        """ Checks pword validity """
        if self.password is None:
            return False
        return check_password_hash(self.password, _password)

    @classmethod
    def authenticate(self, _email, _password):
        """ Checks if the user is authenticated """
        user = Users.query.filter(Users.email == _email).first()
        is_auth = False

        if user:
            is_auth = user.is_password_valid(_password)

        return user, is_auth

    @classmethod
    def email_exists(self, _email):
        return db.session.query(
            db.exists().where(Users.email==_email)).scalar()

