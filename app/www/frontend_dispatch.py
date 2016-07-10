# Import flask dependencies
from flask import Blueprint
from flask import render_template
from flask_login import login_required

# Define the blueprint: 'auth', set its url prefix: app.url/user
mod_frontend = Blueprint('frontend', __name__)


# You can declare all the frontend routes here

@mod_frontend.route('/login', methods=['GET'])
def login_page():
    return render_template('pages/login.html')

@mod_frontend.route('/signup', methods=['GET'])
def signup_page():
    return render_template('pages/signup.html')

@mod_frontend.route('/profile', methods=['GET'])
@login_required
def user_profile():
    return render_template('pages/profile.html')