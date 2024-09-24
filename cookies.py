import requests

url = "https://httpbin.org/cookies"

cookies = {'location' : 'New York'}

# r = requests.get(url, cookies=cookies)
# print(r.text)

r2 = requests.get('https://www.google.com')
print(r2.cookies['1P_JAR'])

requestsJar = requests.cookies.RequestsCookieJar()

requestsJar.set("userId", "John99", domain="httpbin.org", path="/cookies")

r3 = requests.get(url, cookies=requestsJar)
print(r3.text)