from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

PORT = 9000

def myApp(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    return ret

httpd = make_server('', PORT, myApp)
print "Serving on port" + PORT + "...."


httpd.serve_forever()