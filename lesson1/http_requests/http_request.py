# https://www.youtube.com/watch?v=BgHzGpiuFYg&feature=youtu.be

import requests
import os

# r = requests.get('https://lambdaschool.com')
r = requests.get('https://google.com')

print("Status Code: {}".format(r.status_code))
print("Response: {}".format(r))
print(r.text)
