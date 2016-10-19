from api import APIClass
from common import *
import json

class items(APIClass):
	def get(self, req, res):
		status = STATUS_OK
		headers = [('Content-type', 'text/plain')]
		res(status, headers)
		return "this is GET /items"

	def post(self, req, res):
		headers = [('Content-type', 'text/json')]
		res(STATUS_OK, headers)
		newItem = {}
		newItem['id'] = 1234
		newItem['name'] = ''
		newItem['price'] = ''
		newItem['brandId'] = ''
		return json.dumps(newItem)

	def put(self, req, res):
		headers = [('Content-type', 'text/json')]
		res(STATUS_OK, headers)
		
		return ""
		
		
	
