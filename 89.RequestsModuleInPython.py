# In this class we shall learn about the requests module in python.

import requests
# response = requests.get("https://www.codewithharry/.com")
# print(response.text)
#
# url = "https://jsonplaceholder.typicode.com/posts"
#
# response = requests.post(url)
# print(response.text)

req = requests.get("https://www.google.com")
print(req.text)

url = "https://www.instagram.com"

requesta = requests.get(url)
print(requesta.text)