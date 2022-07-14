from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
	# This is a built-in method in BaseHTTPRequestHandler.  Hence, caps.
	def do_GET(self):
		"""
		Arguments:
			Country: name of country via url (optional)
			Capital: name of capital city via url (optional)

		Returns:
			Encoded message
		"""
		s = self.path
		url_components = parse.urlsplit(s)
		query_string_list = parse.parse_qsl(url_components.query)
		dic = dict(query_string_list)

		country = dic.get('country')
		capital = dic.get('capital')

		if "country" in dic:
			r = requests.get(f'https://restcountries.com/v3.1/name/{country}')
			data = r.json()
			for details in data:
				capital_city = details["capital"][0]
			message = str(f'The capital of {country} is {capital_city}')
		elif "capital" in dic:
			r = requests.get(f'https://restcountries.com/v3.1/capital/{capital}')
			data = r.json()
			# Use this format since the name data is a dictionary within the
			# json array.  It will not work calling it from within a for loop
			# with this syntax.
			country_name = data[0]["name"]["official"]
			message = str(f'{capital} is the capital of {country_name}')
		else:
			message = str('Please enter a country or capital in the url in '
						  'the format of "?country=<country>" or '
						  '"?capital=<capital>" (without the quotes).')

		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()

		self.wfile.write(message.encode())
