import requests

endpoint = "http://locolhost:8000/api/"

response = requests.get(endpoint)
print(response.json())