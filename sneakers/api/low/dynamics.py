"""

Prisma Inc.

dynamics.py

Status: UNDER DEVELOPMENT for Major Update Ryzen

Made by Alexis W.

"""

from sneakers.api.low import database
from sneakers.api.low import threading



def update_usd():

    print('Updating database prices, please wait.')
    datab = database.load_database()
    usdprices = datab['USDvalue'].tolist()
    links = datab['link3'].tolist()
    print(len(usdprices))
    print(len(links))
    prices = threading.update_usd_processing(links)
    print(len(prices))
    datab['USDvalue'] = prices
    database.save_database(datab)
    return True

def update_nzd():

    print('Updating database NZD prices, please wait.')
    datab = database.load_database()
    usdprices = datab['USDvalue'].tolist()
    print(len(usdprices))
    nzdprices = threading.update_nzd_processing(usdprices)
    print(len(nzdprices))
    datab['NZDvalue'] = nzdprices
    database.save_database(datab)

    return True


def update_both():

    print('Updating database prices, please wait.')
    datab = database.load_database()
    usdprices = datab['USDvalue'].tolist()
    links = datab['link3'].tolist()
    prices = threading.update_usd_processing(links)
    datab['USDvalue'] = prices
    database.save_database(datab)


    print('Updating database NZD prices, please wait.')
    datab = database.load_database()
    usdprices = datab['USDvalue'].tolist()
    nzdprices = threading.update_nzd_processing(usdprices)
    datab['NZDvalue'] = nzdprices
    database.save_database(datab)
    return True


