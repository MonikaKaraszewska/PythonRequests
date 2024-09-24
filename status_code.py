import requests

r= requests.get("https://xkcd.com/353/")

print(r.status_code)
print(r.ok) # zwroca true ponizej 400 response

print(r.headers)
