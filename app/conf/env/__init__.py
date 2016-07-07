from .development import Development as DevConf
from .staging import Staging as StagingConf
from .production import Production as ProdConf

__all__ = ['get_env']

def get_env(_env):
	""" Switches env """
	CN = {
		'development': DevConf,
		'staging': StagingConf,
		'production': ProdConf
	}
	print(' * Loading {} config'.format(_env))
	return CN[_env]