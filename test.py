import requests

BASE = "http://127.0.0.1:5000/"

res = requests.post('http://localhost:5000/api/add_message/1234', json={"mytext":"lalala"})
if res.ok:
    print(res.json()
