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

def create_training_subfolder(name, parent):

    # parent = 'sneakers/datasets'

    path = os.path.join(parent, name)

    try:

        os.makedirs(path)

        # print("Directory '% s' created" % name)

    except FileExistsError:
        print('Directory already exists! Skipping folder creation...')
        return True
    return True

def create_training_folder(name):

    parent = 'sneakers/datasets'

    path = os.path.join(parent, name)

    try:

        os.makedirs(path)

        print("Directory '% s' created" % name)

    except FileExistsError:
        print('Directory already exists! Skipping folder creation...')
        return True

    return True

def build_dataset(quantity, brandname='None'):
    """
    Builds the dataset for training
    :param brand: If True gets branded if false, well, else.
    :param brandname: Brand name
    :return: Pandas Dataframe
    """

    data = datautils.constructor()

    if brandname is not 'None':

        databranded = data_by_brand(data, brandname)

        data = databranded.iloc[:quantity]


    else:

        pass

    return data

def build_tf_training(dataset, title):

    create_training_folder(title)

    processing.img_downloader_training(dataset, 'sneakers/datasets/{ftitle}'.format(ftitle=title))



    return ':p'
