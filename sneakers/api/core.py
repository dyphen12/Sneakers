"""

Made by Alexis Wong.
Prisma Inc.

"""
import requests
import json
import pandas as pd
import progressbar

# This functions connects to RapidAPI
# Use this functions if there are tokens available for the API


# Status: Checked
def get_response(limit, page):

    url = "https://the-sneaker-database.p.rapidapi.com/sneakers"

    querystring = {"limit": limit, "page": page}

    header = {
        'x-rapidapi-key': "d95141d382mshab73dd2df74b5dfp131a06jsn567d929b49db",
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
def update_shoes_db(quantity):  # -----> String

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

        df.to_csv('sneakers/datasets/sneakers-100000-extended.csv')

    return True
