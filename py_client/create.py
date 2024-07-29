import requests

headers = {'Authorization': 'Bearer 860e9066635f3b982e44d8b47a90518f433232d0'}
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "2023 Benz",
    "price": 45.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())