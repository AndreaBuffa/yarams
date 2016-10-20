import requests
from common import *
import json

SERVER = "localhost:9000"
OK = 200

context = []

def test(method, path, params):
	global context
	if method == 'get':
		res = requests.get('http://' + SERVER + path)
	elif method == 'delete':
		res = requests.delete('http://' + SERVER + path)
	elif method == 'put':
		context['name'] = 'my beautiful shoes'
		res = requests.put('http://' + SERVER + path,
							data = json.dumps(context))
	elif method == 'post':
		res = requests.post('https://' + SERVER + path)

	print "****** " + method.upper() + ' ' + path + params

	print res.status_code

	if res.status_code == OK:
		context = json.loads(res.content)
		print res.content
		print "SUCCESS"
	else:
		print "FAILED"
		exit()

# CREATE a new item
test('post', '/api_example1/v1/items', '')

# EDIT a new item
test('put', '/api_example1/v1/items/' + str(context['id']), '')
# View a particular item
test('get', '/api_example1/v1/items/' + str(context['id']), '')
# View all items
test('get', '/api_example1/v1/items', '')
# DEL
test('delete', '/api_example1/v1/items', '')
