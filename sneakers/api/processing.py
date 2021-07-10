"""

Made by Alexis Wong.
Prisma Inc.

"""
import multiprocessing
from multiprocessing import Pool
from multiprocessing import Process

import pandas as pd
import os
import requests
import progressbar
import time
import gc
from PIL import Image
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as pyImage


def processing_xlsx(df, ws):

    process_list = img_pre_multiprocess(df, ws)

    with Pool(5) as p:
        print(p.map(img_multiprocess, process_list))

    return True


def img_pre_multiprocess(df, ws):

    time.sleep(4)

    # Progress Bar Object
    progsc = progressbar

    cellprocess = []

    for i in progsc.progressbar(range(0, len(df.index))):

        url = df['image'][i]

        j = i + 2

        cellname = 'S{fnum}'.format(fnum=j)

        cellprocess.append([cellname, url, ws])

    return cellprocess


def img_process(df, path):

    wb = load_workbook(filename=path)

    ws = wb.active

    # Progress Bar Object
    progsc = progressbar

    for i in progsc.progressbar(range(0, len(df.index))):

        url = df['image'][i]

        j = i + 2

        cellName = 'S{fnum}'.format(fnum=j)

        try:

            im = Image.open(requests.get(url, stream=True).raw)

            im_100 = im.resize((78, 100))

            loc = "img/Sneaker{}.png".format(j)

            im_100.save(loc, format="png")

            img = Image.open(loc)

            xImg = pyImage(img)

            ws[cellName] = ''

            ws.add_image(xImg, cellName)

            wb.save(path)

            del cellName
            del url
            del im_100
            del im

            gc.collect()

        except requests.exceptions.MissingSchema:

            pass

        except requests.exceptions.ConnectionError:

            time.sleep(10)

            pass


# DEV

def img_multiprocess(processes):

    cellName = processes[0]
    url = processes[1]
    ws = processes[2]

    try:

        im = Image.open(requests.get(url, stream=True).raw)

        im_100 = im.resize((78, 100))

        loc = "img/Sneaker{}.png".format(cellName)

        im_100.save(loc, format="png")

        img = Image.open(loc)

        xImg = pyImage(img)

        ws[cellName] = ''

        ws.add_image(xImg, cellName)

        return 'Image added to {fimg} succesfully!'.format(fimg=cellName)

    except requests.exceptions.MissingSchema:

        return 'The cell {fimg} is MissingSchema :('.format(fimg=cellName)

    except requests.exceptions.ConnectionError:

        return 'The cell {fimg} gives ConnectionError :('.format(fimg=cellName)
