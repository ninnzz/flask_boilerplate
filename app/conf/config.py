import os
from .constants import INSTANCE_FOLDER_PATH

class BaseConfig(object):

	# App name
	APP_NAME = "Python Flask Boilerplate"

	# Get app root path, also can use flask.root_path.
	BASE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/../'

	DEBUG = False
	TESTING = False
	THREADS_PER_PAGE = 2

	AUTHOR = ['nreclarin@gmail.com']

	APP_ENV = 'development'


class DefaultConfig(BaseConfig):

	# Statement for enabling the development environment
	DEBUG = True

	CSRF_ENABLED = True
	CSRF_SESSION_KEY = 'jUZts0meR@nd0mK3yz'
	SECRET_KEY = 'jUZts0meR@nd0mK3yz'

	PAGE_LIMIT = 20

	# CORS
	ALLOWED_HEADERS = ['Access-Token', 'Content-Type', 'referrer']
	ALLOWED_ORIGINS = '*'
	ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE']

	ERROR = {
		'no_results': 'No results found',
		'permission': 'You do not have permission to do this action'
	}
	
	SQLALCHEMY_TRACK_MODIFICATIONS = False

print(' * Loading base config')