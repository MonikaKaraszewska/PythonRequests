import requests

r = requests.get("https://httpbin.org/basic-auth/corney/testing", auth =('corney', 'testing'))

print(r)

print("....")
print(r.text)
