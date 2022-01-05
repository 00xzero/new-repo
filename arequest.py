import requests
from pprint import pprint

projects = ['doodles-official', 'mutant-ape-yacht-club', 'cool-cats-nft','alienfrensnft', 'deadfellaz', 'critterznft', 'coolmans-universe', 'little-lemon-friends', 'cryptomories', 'animo-official' ]


for nft in projects:
    url = f"https://api.opensea.io/api/v1/collection/{nft}"
    response = requests.request("GET", url)
    floorprice = response.json()['collection']['stats']['floor_price']
    print(f"{nft} floor: {floorprice} ETH")