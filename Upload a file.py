import requests

# payload = {"firstName": "Tom", "lastName" : "Smith"}
#
# r = requests.post("https://httpbin.org/post",data=payload)
# print(r.status_code)
# print(r.text)

url = "https://httpbin.org/post"

# files = {'file': open('Book2.csv', 'rb')}
#
# r = requests.post(url,files=files)
# print(r.status_code)
# print(r.text)


'''upload kilka plików na raz'''

# files = {
#     ('file1',('Book2.csv', open('Book2.csv', 'rb'), 'csv')),
#     ('file2',('books_title.csv', open('Book2.csv', 'rb'), 'csv'))
#          }
#
# r = requests.post(url,files=files)
# print(r.status_code)
# print(r.text)

'''nie wiem o co tu chodzi'''
files1 = {'copy': ('test_upload.txt', 'co to ')}
getdata = requests.post(url, files=files1)
print(getdata.text)