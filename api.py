from common import *

def build404Res(start_response):
	headers = [('Content-type', 'text/plain')]
	start_response(STATUS_NOT_FOUND, headers)
	return ""

class APIClass():

	def get(self, req, res):
		return build404Res(start_response)

	def post(self, req, res):
		return build404Res(start_response)

	def put(self, req, res):
		return build404Res(start_response)

	def delete(self, req, res):
		return build404Res(start_response)
