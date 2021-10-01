"""

Prisma Inc.

builder.py

Status: UNDER DEVELOPMENT for Major Update Ryzen

Made by Alexis W.

"""

from sneakers.api.low import database

import json

def build_dataset():
    datab = database.load_database()
    #datab.reset_index(drop=True, inplace=True)
    datab = datab.set_index('id')
    result = datab.to_json(orient='index')
    parsed = json.loads(result)
    build = json.dumps(parsed, indent=4)

    return parsed


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