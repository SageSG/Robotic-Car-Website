import requests

BASE = "http://127.0.0.1:5000/"
input()
response = requests.get(BASE)
print(response)

