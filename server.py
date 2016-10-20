from eventlet import wsgi
import eventlet
from common import *

def myApp(environ, start_response):

	#setup_testing_defaults(environ)
	#headers = [('Content-type', 'text/plain')]
	#start_response('200 OK', headers)
	#ret = ["%s: %s\n" % (key, value)
		#for key, value in environ.iteritems()]
	#return ret

	if environ['PATH_INFO']:
		path = environ['PATH_INFO']
		pathTokens = path.split("/")
		if len(pathTokens) < 3:
			return "ERROR: PATH must be in this form api_name/version/methodname"
		#ret = ["%s\n" % (value) for value in pathTokens]
		import importlib
		importlib.import_module('api')
		path = '.'.join(map(str, pathTokens[1:4]))
		#print path
		module = importlib.import_module(path)
		classToInst = getattr(module, str(pathTokens[3]))
		api = classToInst()
		return getattr(api, environ['REQUEST_METHOD'].lower()) (environ, start_response)
	else:
		pass

wsgi.server(eventlet.listen(('', PORT)), myApp)

wsgi.server(eventlet.wrap_ssl(eventlet.listen(('', PORT)),
	certfile='cert.crt',
	keyfile='private.key',
	server_side=True), myApp)
