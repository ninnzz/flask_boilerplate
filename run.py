import os
import sys
from app import init_app

if __name__ == '__main__':

	app = init_app()
	
	if len(sys.argv) > 1:
		app.run(host='0.0.0.0', port=int(sys.argv[1]), 
			use_reloader=False, threaded=True)
	else:
		app.run(host='0.0.0.0', port=3000, 
			use_reloader=True, threaded=True, debug=True)
