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
from PIL import Image
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as pyImage
from sneakers.api import processing
from datetime import datetime


def load_database():
    shoes = pd.read_csv('sneakers/datasets/sneakerstempdb2live.csv', index_col=0, low_memory=False)
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


def get_sneaker_by_name(name):

    sneakers = load_database()

    snkobj = sneakers.loc[sneakers['name'] == name]


    return snkobj




