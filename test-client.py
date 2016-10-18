import requests
from common import *

SERVER = "localhost:9000"
OK = 200

def test(method, path, params):
	if method == 'get':
		res = requests.get('http://' + SERVER + path)
	elif method == 'delete':
		res = requests.delete('http://' + SERVER + path)
	elif method == 'put':
		res = requests.put('http://' + SERVER + path)
	elif method == 'post':
		res = requests.post('http://' + SERVER + path)

	print "****** " + method.upper() + ' ' + path + params

	print res.status_code
	if res.status_code == OK:
		print res.content
		print "SUCCESS"
	else:
		print "FAILED"
		exit()

test('post', '/api_example1/v1/items', '')
test('put', '/api_example1/v1/items', '')
test('get', '/api_example1/v1/items', '')
test('delete', '/api_example1/v1/items', '')
