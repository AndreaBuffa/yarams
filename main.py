from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

PORT = 9000

def myApp(environ, start_response):
	setup_testing_defaults(environ)
	status = '200 OK'
	headers = [('Content-type', 'text/plain')]
	start_response(status, headers)
	import api_example1.v1
	if environ['PATH_INFO']:
		path = environ['PATH_INFO']
		pathTokens = path.split("/")
		if len(pathTokens) < 3:
			return "ERROR: PATH must be in this form api_name/version/methodname"
		#ret = ["%s\n" % (value) for value in pathTokens]
		import importlib
		path = '.'.join(map(str, pathTokens[1:]))
		#print path
		module = importlib.import_module(path)
		classToInst = getattr(module, str(pathTokens[3]))

		api = classToInst()

		return getattr(api, environ['REQUEST_METHOD'].lower()) ()
		if pathTokens:
			return 'cacas'
	else:
		pass

    #ret = ["%s: %s\n" % (key, value)
           #for key, value in environ.iteritems()]
	#return ret

httpd = make_server('', PORT, myApp)

print "Serving on port " + str(PORT) + "...."


httpd.serve_forever()
