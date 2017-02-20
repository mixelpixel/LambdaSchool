# https://www.youtube.com/watch?v=XnUp9BNCQZM

import requests

my_pizza_order = {
    "custname":"patrick",
    "custtel":"1234567890",
    "custemail":"e-mail@e.mail",
    "size":"x-large",
    "topping":"pepperoni",
    "delivery":"14:15",
    "comments":"call when arrive"
}

r1 = requests.post('http://httpbin.org/post', data = my_pizza_order)

print("My pizza order: {}".format(r1.text))

contact_form_json = {
    "name": "Austen",
    "lastname": "Allred",
    "email": "austen.allred@gmail.com",
    "message": "When does the part-time course start?"
}

r2 = requests.post('https://lambdaschool.com/contact-form', data = contact_form_json)

print("Contact form JSON: {}".format(r2.text))

my_blog_post = {
    "subject":"How to learn anything",
    "text":"blah, blah, blah",
    "comments_enabled": True
}

r3 = requests.post('https://posttestserver.com/post.php', data = my_blog_post)

print("My blog post: {}".format(r3.text))
