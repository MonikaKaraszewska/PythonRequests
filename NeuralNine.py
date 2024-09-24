import requests
#
# params = {"name":"Monik", "age":40} # NAZYWAMY PARAMS Do GET - kiedy chcemy uzyskac dane o kokretnych parametrach
#                                         #response = requests.get("https://httpbin.org/get",params=params)
#
# payload = {"name":"Asia", "age":15} # payload nzywamy zmienna do wysyłania danych POST, w tedy przy url jst data
#                                     #response = requests.post("https://httpbin.org/post",data=payload)
# response = requests.post("https://httpbin.org/post",data=payload)
#
# # print(response)
# # print(response.status_code)
# print(response.url)
# print(response.text)
# res_json = response.json()
#
#
# del res_json['origin']
# print(res_json)


# response2 = requests.get("https://httpbin.org/status/404")
# print(response2.status_code)
#
# if response2.status_code == requests.codes.not_found:
#     print("Not found")
# else:
#     print(response2.status_code)

print("....user-agent")
#Termin "User-Agent" odnosi się do nagłówka HTTP, który przesyła informacje o używanym przez klienta programie lub
# przeglądarce. Nagłówek ten zawiera identyfikator, który pozwala serwerowi rozpoznać rodzaj i wersję klienta,
# a także inne informacje, takie jak system operacyjny.
# jak w user-agent jest Python to stronamoze cie zablokowac, albo inaczej odpowiadac na zapytania z pytona a nie z przegladarki
#i mozna zdefiniowac manualnie useragent, przy wysyałnu zadania, musimy wiec wyslacswoje headers

# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
# response_user_agent = requests.get("https://httpbin.org/user-agent", headers=headers)
# print(response_user_agent.text)


print("images........................")
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Accept" : "image/jpeg"
# }
# response_image = requests.get("https://httpbin.org/image", headers=headers)
#
#
# with open("muimage.jpeg", "wb") as f:
#     f.write(response_image.content)

print("........................delay")

response_delay = requests.get("https://httpbin.org/delay/2", timeout=3)

print(response_delay)