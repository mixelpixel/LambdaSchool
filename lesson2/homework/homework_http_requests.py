# https://github.com/SunJieMing/python-minicamp-homework-2

import requests

url = 'http://127.0.0.1:5000/'

get_it = requests.get(url)

print(get_it.text)

bday_url = url + 'birthday'

print(requests.get(bday_url).text)

print(requests.get(url + 'greeting/Patrick').text)
print('Greeting Response: {}'.format(requests.get(url + 'greeting/Patrick')))
print('Greeting Status Code: {}'.format(requests.get(url + 'greeting/Patrick').status_code))
