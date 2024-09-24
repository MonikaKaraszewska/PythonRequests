'''https://www.youtube.com/playlist?list=PLIMhDiITmNrILoYaVsrxwteH6LqMr07uX'''
import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response)

"parse response to jsnon format"
print("........json")
json_response = json.loads(response.text)
print(json_response)

print("...jsonPATH")
pages = jsonpath.jsonpath(json_response, 'total_pages')
assert pages[0] == 2
