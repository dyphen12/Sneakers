"""

Prisma Inc. 2021

core.py

Status: Checked

Note: The core of the API, is the connection to RapidAPI and the online databases.

Made by Alexis W.

"""
import requests
import json
import pandas as pd
import progressbar

# Connections to RapidAPI
# Works as the API core, the Sneakers Data.
# Use this methods to Update and Set-up the API data.

class Config:
    def __init__(self, dbs, imglit, apik, inys, localimg, airkey, airbasekey):
        self.dbsize = dbs
        self.imglitter = imglit
        self.apikey = apik
        self.inysize = inys
        self.localimg = localimg
        self.airkey = airkey
        self.airbasekey = airbasekey


def load_config():
    config_loc = 'sneakers/config.json'
    try:
        with open(config_loc) as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()

        dbsize = jsonObject['api-config']['db-size']
        imagelitter = jsonObject['api-config']['image-row-litter']
        apikey = jsonObject['api-config']['api-key']
        inysize = jsonObject['api-config']['iny-base-size']
        localimg = jsonObject['api-config']['local-imaging']
        airkey = jsonObject['api-config']['air-key']
        airbasekey = jsonObject['api-config']['airbase-key']

        cf = Config(dbsize, imagelitter, apikey, inysize, localimg, airkey, airbasekey)

        return cf

    except FileNotFoundError:
        print('Config not found.')


# Status: Checked
def get_response(limit, page):

    url = "https://the-sneaker-database.p.rapidapi.com/sneakers"

    querystring = {"limit": limit, "page": page}

    cf = load_config()

    header = {
        'x-rapidapi-key': cf.apikey,
        'x-rapidapi-host': "the-sneaker-database.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=header, params=querystring)

    return response


# Status: Checked
def get_shoes(quantity):  # -----> String

    ShoeList = []

    numquantity = int(quantity)

    if int(quantity) <= 100:

        response = get_response(limit='100', page='1')
        shoes = json.loads(response.text)
        ShoeList = shoes['results']
        # print(ShoeList)

    else:

        pages = int((int(quantity) * 1) / 100)

        progress_lenA = pages + 1
        progsa = progressbar

        for i in progsa.progressbar(range(progress_lenA)):

            try:

                response = get_response(limit='100', page=str(i + 1))
                shoes = json.loads(response.text)
                res = shoes['results']

                for item in res:
                    ShoeList.append(item)

            except:
                pass

    df = pd.DataFrame(
        columns=['brand', 'estimatedMarketValue', 'gender', 'id', 'image', 'thumbnail', 'link1', 'link2', 'link3',
                 'name', 'colorway', 'releaseDate', 'releaseYear', 'retailPrice', 'silhouette', 'sku', 'story'])

    progress_lenB = numquantity
    progsB = progressbar

    for i in progsB.progressbar(range(progress_lenB)):
        shoe = ShoeList[i]

        shoeDic = {'brand': shoe['brand'],
                   'estimatedMarketValue': shoe['estimatedMarketValue'],
                   'gender': shoe['gender'],
                   'id': shoe['id'],
                   'image': shoe['image']['original'],
                   'thumbnail': shoe['image']['thumbnail'],
                   'link1': shoe['links']['stockx'],
                   'link2': shoe['links']['flightClub'],
                   'link3': shoe['links']['goat'],
                   'name': shoe['name'],
                   'colorway': shoe['colorway'],
                   'releaseDate': shoe['releaseDate'],
                   'releaseYear': shoe['releaseYear'],
                   'retailPrice': shoe['retailPrice'],
                   'silhouette': shoe['silhouette'],
                   'sku': shoe['sku'],
                   'story': shoe['story']}

        df.loc[i] = shoeDic

    return df


# Status: Checked
def update_shoes_db():  # -----> String

    cf = load_config()

    quantity = cf.dbsize

    ShoeList = []

    numquantity = int(quantity)

    if int(quantity) <= 100:

        response = get_response(limit='100', page='1')
        shoes = json.loads(response.text)
        ShoeList = shoes['results']
        # print(ShoeList)

    else:

        pages = int((int(quantity) * 1) / 100)

        progress_lenA = pages + 1
        progsa = progressbar

        for i in progsa.progressbar(range(progress_lenA)):

            try:

                response = get_response(limit='100', page=str(i + 1))
                shoes = json.loads(response.text)
                res = shoes['results']

                for item in res:
                    ShoeList.append(item)

            except:
                pass

    df = pd.DataFrame(
        columns=['brand', 'estimatedMarketValue', 'gender', 'id', 'image', 'thumbnail', 'link1', 'link2', 'link3',
                 'name', 'colorway', 'releaseDate', 'releaseYear', 'retailPrice', 'silhouette', 'sku', 'story'])

    progress_lenB = numquantity
    progsB = progressbar

    for i in progsB.progressbar(range(progress_lenB)):
        shoe = ShoeList[i]

        shoeDic = {'brand': shoe['brand'],
                   'estimatedMarketValue': shoe['estimatedMarketValue'],
                   'gender': shoe['gender'],
                   'id': shoe['id'],
                   'image': shoe['image']['original'],
                   'thumbnail': shoe['image']['thumbnail'],
                   'link1': shoe['links']['stockx'],
                   'link2': shoe['links']['flightClub'],
                   'link3': shoe['links']['goat'],
                   'name': shoe['name'],
                   'colorway': shoe['colorway'],
                   'releaseDate': shoe['releaseDate'],
                   'releaseYear': shoe['releaseYear'],
                   'retailPrice': shoe['retailPrice'],
                   'silhouette': shoe['silhouette'],
                   'sku': shoe['sku'],
                   'story': shoe['story']}

        df.loc[i] = shoeDic

        df.to_csv('sneakers/datasets/sneakers-local-db.csv')

    return True


def get_shoe_by_id(snid):

    cf = load_config()

    url = "https://the-sneaker-database.p.rapidapi.com/sneakers/{fid}".format(fid=snid)

    header = {
        'x-rapidapi-key': cf.apikey,
        'x-rapidapi-host': "the-sneaker-database.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=header)

    sneaker = json.loads(response.text)

    return sneaker['results']


def api_version():
    version = '4.5.0a'
    return version