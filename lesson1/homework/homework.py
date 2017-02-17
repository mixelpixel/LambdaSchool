import requests
import os

r = requests.get('https://google.com')

to_file = r.text

text_file = open("webpage.html", "w")
text_file.write(to_file)
text_file.close()
os.system("open "+"webpage.html")
