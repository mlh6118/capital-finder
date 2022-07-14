from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
	# This is a built-in method in BaseHTTPRequestHandler.  Hence, caps.
	def do_GET(self):
		s = self.path
		url_components = parse.urlsplit(s)
		query_string_list = parse.parse_qsl(url_components.query)
		dic = dict(query_string_list)

		country = dic.get('country')
		capital = dic.get('capital')

		if country:
			requests.get('https://restcountries.com/v3.1/name/{country}')
		elif capital:
			requests.get('https://restcountries.com/v3.1/name/{capital}')

		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()

		self.wfile.write(message.encode())
