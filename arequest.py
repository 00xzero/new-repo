import requests
from pprint import pprint

url = "https://api.opensea.io/api/v1/collection/doodles-official"

response = requests.request("GET", url)

pprint(response.json()['collection']['stats']['floor_price'])