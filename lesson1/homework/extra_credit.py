import requests

contact_info = {
    "email": "mixelpix@mac.com",
    "lastname": "Kennedy",
    "message": "Thanks for putting together this awesome course - it's a lot of fun!",
    "name": "Patrick",
}

r = requests.post('https://lambdaschool.com/contact-form', json = contact_info)

print("response: %s status code: %s" % (r.text, r.status_code))
