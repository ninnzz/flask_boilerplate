# System import
import os

# Import flask
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from .conf import config as Config
from .conf import constants as CONST
from .conf.env import get_env

from .lib.database import db
from .lib.error_handler import mod_err, FailedRequest

from .api.user.model import Users


# import *
__all__ = ['init_app']


def init_app(config=None):
	""" App initialization """

	# Declare app
	app = Flask(Config.BaseConfig.APP_NAME, 
		instance_path=CONST.INSTANCE_FOLDER_PATH, 
		instance_relative_config=True,
		template_folder= Config.BaseConfig.BASE_DIR + CONST.TEMPLATE_FOLDER)

	load_config(app, config)
	load_middlewares(app)
	load_lib(app)
	load_blueprints(app)

	return app


def load_config(app, config=None):
	""" Load the base config and env config """

	app.config.from_object(Config.DefaultConfig)

	# Loads config file if there are any config included
	if config:
		app.config.from_object(config)
		print(' * Loading custom config')
		return

	env = Config.BaseConfig.APP_ENV

	# checks available environment
	if os.environ.get('NMI_ENV') is not None:
		env = os.environ.get('NMI_ENV').lower()

	app.config.from_object(get_env(env))


def load_lib(app):
    """ lib for application """

    # Database SQLAlchemy
    # If you want to use raw engine creation
    # Use create_engine from .lib.database
    db.init_app(app)

    # Loads the flask-login
    login_manager = LoginManager()
    
    @login_manager.user_loader
    def _get_user(id):
        return Users.query.get(id)


    @login_manager.unauthorized_handler
    def no_permission(msg=None):
        raise FailedRequest('Ooops, sorry. You\'re not authorized!',401)

    login_manager.setup_app(app)


def load_middlewares(app):
	""" Loads necessary middle wares for the app """

	# Error handlers
	app.register_blueprint(mod_err)

	# CORS
	CORS(app, allow_headers=app.config['ALLOWED_HEADERS'], 
		origins=app.config['ALLOWED_ORIGINS'], 
		methods=app.config['ALLOWED_METHODS'])

	@app.before_request
	def before():
		# Preloading of stuff if any
		# You can put custom session here if you want
		pass


def load_blueprints(app):
    """ Loads blueprints for the app """
    from .www.frontend_dispatch import mod_frontend as frontend_module
    from .api.auth.dispatch import mod_auth as auth_module
    from .api.user.dispatch import mod_user as user_module

    app.register_blueprint(frontend_module, url_prefix='/pages')
    app.register_blueprint(auth_module, url_prefix='/api/auth')
    app.register_blueprint(user_module, url_prefix='/api/user')

