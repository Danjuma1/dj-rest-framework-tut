import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "2023 Benz",
    "price": 45.99
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())