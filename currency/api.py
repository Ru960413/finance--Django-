# interact with exchange rate currency api
import requests

api_key = "de854dd1ac96a4c45b041347"

url = 'https://v6.exchangerate-api.com/v6/${api_key}/latest/TWD'

response = requests.get(url)
data = response.json()

