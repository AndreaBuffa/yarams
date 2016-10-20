from api import APIClass
from common import *
import json

class items(APIClass):
	def get(self, req, res):
		status = STATUS_OK
		headers = [('Content-type', 'text/json')]
		res(status, headers)
		return "[]"

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
		try:
			request_body_size = int(req.get('CONTENT_LENGTH', 0))
		except (ValueError):
			request_body_size = 0

		request_body = req['wsgi.input'].read(request_body_size)
		data = json.loads(request_body)
		#data['id']		
		return json.dumps(data)
		
		
	
