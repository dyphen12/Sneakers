"""

Prisma Inc.

database.py

Status: UNDER DEVELOPMENT for Major Update Ryzen

Made by Alexis W.

"""

import pandas as pd
import os
import requests
import progressbar
import gc
import pymongo
import gridfs
from pprint import pprint
import json
import certifi
from sneakers.api.low import builder as bd
from sneakers.api.low import threading as thr
import base64
import bson
from bson.binary import Binary
from bson.json_util import dumps, loads


ca = certifi.where()

#--------- MONGO DB IMPLEMENTATION -----------------

snkclient = pymongo.MongoClient("mongodb+srv://Prismadevops:tetas1@sneakercluster.iuykn.mongodb.net/stockdotshopdb?retryWrites=true&w=majority", tlsCAFile=ca)

snkdb=snkclient['stockdotshopdb']
snkcoll = snkdb['sneakers']
# Issue the serverStatus command and print the results


def core_connection_snk():
    serverStatusResult = snkdb.command("serverStatus")
    pprint(serverStatusResult)
    print(snkdb)
    return'8=======D'

def load_database_ryzen():
    sneakerscur = list(snkcoll.find({}))
    # Calling DataFrame constructor on list
    sneakers = pd.DataFrame(sneakerscur)
    return sneakers



def search_query_database(query):

    myquery2 = {"$text" : {"$search": query}}

    resultcursor = list(snkcoll.find(myquery2).limit(100))

    result = pd.DataFrame(resultcursor)

    return result



def get_page_database_ryzen(x):

    # myquery2 = {"$text" : {"$search": query}}

    resultcursor = list(snkcoll.find().skip(x).limit(100))

    result = pd.DataFrame(resultcursor)

    return result


def get_sneaker_by_sku(sku):

    myquery2 = {"sku": sku}

    q3 = {"sku": {"$in": sku}}

    resultcursor = list(snkcoll.find(q3))

    result = pd.DataFrame(resultcursor)

    return result


#---------- LEGACY PANDAS -----------------------
def load_database():
    shoes = pd.read_csv('sneakers/datasets/sneakerstempdb2live.csv', low_memory=False)
    return shoes

def save_database(df):
    df.to_csv('sneakers/datasets/sneakerstempdb2live.csv', index=False)
    print('Database has been modified and saved.')
    return True

def load_newdatabase():
    shoes = pd.read_csv('sneakers/datasets/sneakersdev1.csv', index_col=0, low_memory=False)
    newsho = shoes.iloc[:10000]
    newsho.to_csv('sneakers/datasets/sneakersdevout.csv', index=False)
    return shoes


def update_csv():
    shoes = pd.read_csv('sneakers/datasets/sneakerstempdb2live.csv', low_memory=False)
    usd_prices = shoes['estimatedMarketValue']
    shoes['USDvalue'] = usd_prices
    shoes['NZDvalue'] = shoes['USDvalue'].apply(lambda x: x * 1.44)
    shoes.to_csv('sneakers/datasets/sneakersfulldb.csv', index=False)
    return shoes



def get_sneaker_by_name(name):

    sneakers = load_database()

    snkobj = sneakers.loc[sneakers['name'] == name]


    return snkobj

def save_database_but_json():
    shu = load_database()
    shu = shu.set_index('id')
    shutomongo = shu.to_json(orient='index')
    parsed = json.loads(shutomongo)

    json_comp = parsed

    with open('sneakers/datasets/sneakers-json/dataset.json', 'w', encoding='utf-8') as f:
        json.dump(json_comp, f, ensure_ascii=False, indent=4)

    print('Database has been modified and saved.')
    return True