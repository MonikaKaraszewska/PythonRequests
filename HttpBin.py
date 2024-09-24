import requests

# payload = {'page': 2, 'count': 25}
# r = requests.get("https://httpbin.org/get",params=payload)

# print(r.text)
# print(r.url)

payload1 = {'username': 'corney', 'password': 'testing'}
r1 = requests.post("https://httpbin.org/post",params=payload1)
# print(r1.text)
r1_dict = r1.json()
print(r1)
print(r1_dict)
print(r1_dict['args'])
print(r1_dict['args']['password'])