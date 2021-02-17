import requests
import json

burl = "https://api.coingecko.com/api/v3"
tickers = ["the-graph", "republic-protocol"]

if __name__ == '__main__':
    for currency in tickers:
        endpoint = "/coins/{}/tickers".format(currency)
        url = burl + endpoint
        res = requests.get(url)
        ticker_details = res.json()

        fname = "notebooks/{}.json".format(currency)

        with open(fname, "w") as tdata:
            json.dump(ticker_details, tdata)
