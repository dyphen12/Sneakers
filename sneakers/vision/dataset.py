"""

Prisma Inc. 2021

dataset.py

Status: Under Development

Made by Alexis W.

"""
from sneakers.api import processing
from sneakers.api import datautils
import os


def data_by_brand(dataset, brandname):
    """
    Loads dataset by a brandname
    :param dataset: Pandas dataframe
    :param brandname: Sneaker Brand
    :return: Pandas dataframe selected
    """

    fwsetv = dataset.loc[dataset['brand'] == brandname]

    return fwsetv

def create_training_folder(name):

    parent = 'sneakers/datasets'

    path = os.path.join(parent, name)

    os.makedirs(path)

    print("Directory '% s' created" % name)
    return True

def build_dataset(brand=False, brandname='none'):
    """
    Builds the dataset for training
    :param brand: If True gets branded if false, well, else.
    :param brandname: Brand name
    :return: Pandas Dataframe
    """

    data = datautils.constructor()

    if brand is True:

        databranded = data_by_brand(data, brandname)

        data = databranded

        print(data)

    else:

        pass

    return data

def build_training(dataset, title):

    # create_training_folder(title)

    processing.img_downloader_training(dataset, 'sneakers/datasets/sheit')





    return ':p'
