"""

Prisma Inc.

threading.py

Status: UNDER DEVELOPMENT for Major Update Ryzen

Made by Alexis W.

"""

from multiprocessing import Pool

from sneakers.api.low import database
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json


def get_price_silence(urlprocess):

    url = urlprocess

    newprice = 0

    try:

        ua = UserAgent()
        # print(ua.chrome)
        header = {'User-Agent': str(ua.chrome)}

        headers = {
            'User-Agent': 'Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US'}

        r = requests.request("GET", url, headers=headers)

        data = r.text

        print(r)

        soup = BeautifulSoup(data, features="lxml")

        # print(soup.text)

        # print(soup.findAll())

        data = soup.find('script', type='application/ld+json')

        # print(soup.find('script', type='application/ld+json').string)

        # print(type(data.string))

        result = json.loads(data.string)

        # print(type(result))

        offer = result['offers']['offers'][1]

        newprice = offer['price']

        return newprice

    except Exception as e:
        # print(e)
        return newprice

def get_nzd_price(priceprocess):

    usdprice = priceprocess

    newprice = usdprice * 1.42

    return newprice


def update_usd_processing(processes):

    prices = []

    with Pool(5) as p:

        print('MULTI-THREADING PROCESS STARTED')
        print('Please wait...')
        for price in p.map(get_price_silence, processes):
            print('Price Obtained: {fprice}'.format(fprice=str(price)))
            prices.append(price)
    return prices

def update_nzd_processing(processes):

    prices = []

    with Pool(5) as p:

        print('MULTI-THREADING PROCESS STARTED')
        print('Please wait...')
        for price in p.map(get_nzd_price, processes):
            print('Price Obtained: {fprice}'.format(fprice=str(price)))
            prices.append(price)
    return prices