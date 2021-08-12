"""

Prisma Inc. 2021

ticker.py

Status: Under Development

Made by Alexis W.

"""

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


def get_price(url):

    ua = UserAgent()
    print(ua.chrome)
    header = {'User-Agent': str(ua.chrome)}

    headers = {'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}

    r = requests.request("GET", url, headers=headers)

    print(r.status_code)

    data = r.text

    soup = BeautifulSoup(data, features="lxml")

    print(soup.text)



