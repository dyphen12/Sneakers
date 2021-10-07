"""

Prisma Inc.

builder.py

Status: UNDER DEVELOPMENT for Major Update Ryzen

Made by Alexis W.

"""
from sneakers.api.low import database

import json
import pandas as pd


# ------- MongoDB Ryzen -------

def build_dataset_ryzen():

    datab = database.load_database_ryzen()
    datab.reset_index(drop=True, inplace=True)
    datab = datab.set_index('_id')
    result = datab.to_json(orient='index')
    parsed = json.loads(result)
    #build = json.dumps(parsed, indent=4)

    #print(parsed)

    return parsed


def build_dataset_pages_ryzen(page):

    perpage = 100

    ind = page*perpage

    build = build_dataset_index_ryzen_v2(ind)

    return build

def build_dataset_index_ryzen(index , ppage):
    datab = database.load_database_ryzen()
    perpage = ppage
    xfrom = index
    xto = int(index+perpage)
    datab2 = datab.iloc[xfrom:xto]
    # datab.reset_index(drop=True, inplace=True)
    datab2 = datab2.set_index('_id')
    result = datab2.to_json(orient='index')
    parsed = json.loads(result)
    build = json.dumps(parsed, indent=4)
    return parsed

def build_userdataset_ryzen(userdataset):

    datab = userdataset
    #datab.reset_index(drop=True, inplace=True)

    if datab.empty:
        return False
    else:

        try:
            datab = datab.set_index('_id')
        except KeyError:
            return False

        result = datab.to_json(orient='index')
        parsed = json.loads(result)
        build = json.dumps(parsed, indent=4)

        return parsed


def build_search_ryzen(query):


    datab = database.search_query_database(query)

    if datab.empty:
        return False

    #datab.reset_index(drop=True, inplace=True)
    try:
        datab = datab.set_index('_id')

        result = datab.to_json(orient='index')
        parsed = json.loads(result)
        # build = json.dumps(parsed, indent=4)

        return parsed
    except KeyError as e:
        return False

def build_dataset_index_ryzen_v2(index):
    datab2 = database.get_page_database_ryzen(index)
    # datab.reset_index(drop=True, inplace=True)
    datab2 = datab2.set_index('_id')
    result = datab2.to_json(orient='index')
    parsed = json.loads(result)
    build = json.dumps(parsed, indent=4)
    return parsed

# ------- LEGACY -------

def build_dataset():

    datab = database.load_database()
    #datab.reset_index(drop=True, inplace=True)
    datab = datab.set_index('id')
    result = datab.to_json(orient='index')
    parsed = json.loads(result)
    build = json.dumps(parsed, indent=4)

    return parsed

def build_dataset_but_parsed():

    datab = database.load_database()
    #datab.reset_index(drop=True, inplace=True)
    datab = datab.set_index('id')
    result = datab.to_json(orient='index')
    parsed = json.loads(result)
    build = json.dumps(parsed, indent=4)

    return build

def build_dataset_index(index , ppage):
    datab = database.load_database()
    perpage = ppage
    xfrom = index
    xto = int(index+perpage)
    datab2 = datab.iloc[xfrom:xto]
    # datab.reset_index(drop=True, inplace=True)
    datab2 = datab2.set_index('id')
    result = datab2.to_json(orient='index')
    parsed = json.loads(result)
    build = json.dumps(parsed, indent=4)
    return parsed

def build_dataset_pages(page):

    perpage = 100

    ind = page*perpage

    build = build_dataset_index(ind, perpage)

    return build


def build_userdataset(userdataset):
    datab = userdataset
    #datab.reset_index(drop=True, inplace=True)
    datab = datab.set_index('id')

    result = datab.to_json(orient='index')
    parsed = json.loads(result)
    build = json.dumps(parsed, indent=4)

    return parsed


def build_dataset_quant(q):

    datab = database.load_database()
    datab = datab.iloc[:q]
    #datab.reset_index(drop=True, inplace=True)
    datab = datab.set_index('id')
    result = datab.to_json(orient='index')
    parsed = json.loads(result)
    build = json.dumps(parsed, indent=4)

    return parsed

def build_bigdata_pages(page):

    perpage = 1000

    ind = page*perpage

    build = build_dataset_index(ind, perpage)

    return build



def build_dataset_index_parsed(index , ppage):
    datab = database.load_database()
    perpage = ppage
    xfrom = index
    xto = int(index+perpage)
    datab2 = datab.iloc[xfrom:xto]
    # datab.reset_index(drop=True, inplace=True)
    datab2 = datab2.set_index('id')
    result = datab2.to_json(orient='index')
    parsed = json.loads(result)
    build = json.dumps(parsed, indent=4)
    return build

def build_bigdata_pages_parsed(page):

    perpage = 1000

    ind = page*perpage

    build = build_dataset_index_parsed(ind, perpage)

    return build