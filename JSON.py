import requests
'''retriving specific information from response'''
r = requests.get("https://api.github.com/events")
print(r.status_code)
events = r.json()
print(events[0])
print(events[0]['type'])
print(events[0]['actor'])
print(events[0]['actor']['login'])

print("....................sending json content")

data = {'firstName' : 'John'}

r = requests.post("https://httpbin.org/post", json=data)
print(r.text)
print(r.status_code)
