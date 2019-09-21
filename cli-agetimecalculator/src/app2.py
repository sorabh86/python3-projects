__author__ = 'sorabh86'

import requests

request = requests.get('http://google.com')

print(request.content)