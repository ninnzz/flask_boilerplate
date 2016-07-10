# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint
from flask_login import login_required, login_user, current_user

# Import app-based dependencies
from ...util import utils

# Import core libraries
from ...lib.database import db
from ...lib.decorators import make_response
from ...lib.error_handler import FailedRequest

from .model import Users

# Define the blueprint: 'user', set its url prefix: app.url/user
mod_user = Blueprint('user', __name__)


@mod_user.route('', methods=['POST'])
@make_response
def add_user(res):
    params = utils.get_data(
    	[	
    		'email', 'password', 'first_name',
    		'last_name', 'age'
    	], [], 
    	request.values)
    
    # Add user to database
    if Users.email_exists(params['email']):
        raise FailedRequest('The email is already taken.', 401)

    user = Users(params)
    db.session.add(user)
    db.session.commit()      
        
    return res.send('Successfully added user')
