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
        # print('Directory already exists! Skipping folder creation...')
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


def check_folder_exist(dir_name):

    if os.path.isdir(dir_name):
        if not os.listdir(dir_name):
            # print("Directory is empty")
            return False
        else:
            # print("Directory is not empty")
            return True
    else:
        print("Given directory doesn't exist")
        return None

def build_tf_training(dataset, title):

    create_training_folder(title)

    path = 'sneakers/datasets/{ftitle}'.format(ftitle=title)

    # processing.img_downloader_training(dataset, path)

    clean_tf_training(path)

    return ':p'

def clean_tf_training(path):

    arr = os.listdir(path)

    print(arr)

    for arrs in arr:
        npath = os.path.join(path, arrs)
        if check_folder_exist(npath) is False:
            os.rmdir(npath)

    return True

def get_labels(path):

    arr = os.listdir(path)

    return arr

