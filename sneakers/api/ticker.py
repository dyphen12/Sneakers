"""

Prisma Inc. 2021

ticker.py

Status: Under Development

Made by Alexis W.

"""

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json


def get_price_silence(url):

    try:
        ua = UserAgent()
        # print(ua.chrome)
        header = {'User-Agent': str(ua.chrome)}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

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

        # print(result['offers']['offers'][1])

        offer = result['offers']['offers'][1]

        # print(offer['price'])

        return offer['price']

    except Exception as e:
        print(e)
        pass

def get_price(url):

    ua = UserAgent()
    print(ua.chrome)
    header = {'User-Agent': str(ua.chrome)}

    headers = {'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    r = requests.request("GET", url, headers=headers)

    print(r.status_code)

    data = r.text

    soup = BeautifulSoup(data, features="lxml")

    #print(soup.text)

    #print(soup.findAll())

    data = soup.find('script', type='application/ld+json')

    print(soup.find('script', type='application/ld+json').string)

    print(type(data.string))

    result = json.loads(data.string)

    print(type(result))

    print(result['offers']['offers'][1])

    offer = result['offers']['offers'][1]

    print(offer['price'])

    return offer['price']



