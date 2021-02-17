import requests
import json

burl = "https://api.coingecko.com/api/v3"
list = "/coins/list"

if __name__ == '__main__':
    coin_list = burl + list
    res = requests.get(coin_list)
    coin_details = res.json()

    with open("coins_list.json", "w") as cl:
        json.dump(coin_details, cl)
