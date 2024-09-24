import requests
r = requests.options('https://www.w3schools.com/')
print(r.headers.get('Date'))
print(r.headers.get('allow'))

r = requests.head('https://www.w3schools.com/')
print(r.headers)

r = requests.options('https://www.w3schools.com/')
print(r.headers.values())

print("......................post")
# r = requests.post('https://httpbin.org/post', data={"KEY" : '999', "VALUE": '666'})
# print(r.text)
#
# print(".................get")
# r = requests.get('https://httpbin.org/get', params={"KEY" : '999', "VALUE": '666'})
# print(r.text)



print("......................................................1")
# r = requests.get('https://api.github.com/events')
# r = r.json()
# print(r[0]['actor']['login'])
# print(r[:-29])