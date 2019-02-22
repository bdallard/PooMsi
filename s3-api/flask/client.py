import requests

response = requests.get("http://127.0.0.1:5000/list/PierreDurand")

print("Code", response.status_code, ":", response.content)