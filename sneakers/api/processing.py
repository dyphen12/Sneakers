"""

Made by Alexis Wong.
Prisma Inc.

"""
import pandas as pd
import os
import requests
import progressbar
import time
import gc
from PIL import Image
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as pyImage

def dev_big_xlsx(df, ver):

    title = "sneakers-{fver}.xlsx".format(fver=ver)

    path = 'sheets/{ftit}'.format(ftit=title)

    df['pic'] = ''

    writer = pd.ExcelWriter(path, engine='xlsxwriter', options={'strings_to_urls': False})
    df.to_excel(writer)
    writer.close()

    wb = load_workbook(filename=path)

    ws = wb.active

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

    print('Images downloaded succesfully...')
    print('XLSX large builded...')
    print('Check /sheets folder for {ffile}'.format(ffile=path))

    return True