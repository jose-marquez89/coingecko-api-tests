import requests
import json
import datetime

burl = "https://api.coingecko.com/api/v3"
charts = ["the-graph", "republic-protocol"]

if __name__ == '__main__':
    # get more than a year of data if exists
    start = datetime.datetime(2019, 12, 1).timestamp()
    end = datetime.datetime.now().timestamp()
    for currency in charts:
        endpoint = "/coins/{}/market_chart/range?vs_currency=usd&from={}&to={}".format(currency, start, end)
        url = burl + endpoint
        res = requests.get(url)
        chart_details = res.json()

        fname = "notebooks/{}.json".format(currency)

        with open(fname, "w") as tdata:
            json.dump(chart_details, tdata)
