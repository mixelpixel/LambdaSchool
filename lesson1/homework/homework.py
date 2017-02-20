# http://us15.campaign-archive1.com/?u=433649a32bb80af8eb197992a&id=e714723cec&e=ae1781534e

import requests
import os

r = requests.get('https://google.com')

to_file = r.text

text_file = open("webpage.html", "w")
text_file.write(to_file)
text_file.close()
os.system("open "+"webpage.html")
