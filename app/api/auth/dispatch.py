# Import global context
from flask import request, session

# Import flask dependencies
from flask import Blueprint
from flask_login import login_required, login_user, current_user, logout_user

from ...util import utils
from ...lib.decorators import make_response
from ...lib.error_handler import FailedRequest

from ..user.model import Users

# Define the blueprint: 'auth', set its url prefix: app.url/user
mod_auth = Blueprint('auth', __name__)


@mod_auth.route('/login', methods=['POST'])
@make_response
def login(res):
    
    params = utils.get_data(['email', 'password'], [], request.values)

    if current_user.is_authenticated:
        return res.send('You are already logged in.')

    user, is_auth = Users.authenticate(params['email'],
        params['password'])

    if not user:
        raise FailedRequest('Invalid email address', 500)
    if not is_auth:    
        raise FailedRequest('Invalid password', 500)    

    ################### NOTE ###################
    # If you want to implement token based
    # authentication, please insert the code
    # to generate/assign token after this.
    ############################################

    # token_function()

    login_user(user, remember=True)

    return res.send('Successfully logged in.')


@mod_auth.route('/logout', methods=['GET'])
@login_required
@make_response
def logout(res):
    """ logout user """
    session.pop('login', None)
    logout_user()
    return res.send('Successfully logged out')


