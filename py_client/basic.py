import requests 

# endpoint = 'http://httpbin.org/anything'
endpoint = 'http://127.0.0.1:8000/api'

get_response = requests.get(endpoint, json={'product_id': 123}) # HTTP Response
# print(get_response.text) # Prints raw text response endpoint

print(get_response.json())
# print(get_response.status_code)