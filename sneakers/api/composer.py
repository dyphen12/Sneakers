"""

Prisma Inc. 2021

composer.py

Status: Checked

Note: For unit testing purposes.

Made by Alexis W.

"""
import pandas as pd
from openpyxl import load_workbook
from sneakers.api import utils
from sneakers.api import processing
from sneakers.api import core


def chunks(data, n):

    m = int(len(data)/n)

    return [data[x:x+m] for x in range(0, len(data), m)]


# Composer is intended to work only on an Excel Worksheet object environment.
class Composer:
    def __init__(self, title, samplesize=0, create=False):
        self.create = create
        self.samplesize = samplesize
        self.folder = 'workout'
        self.title = title
        self.full_path = 'workout/{ftit}.xlsx'.format(ftit=title)

    def create_workbook(self):
        # Creates a new empty workbook with no sneaker images, just data
        dataset = utils.load_shoes_dataset()
        sample = dataset.iloc[:self.samplesize]

        sample['pic'] = ''
        writer = pd.ExcelWriter(self.full_path, engine='xlsxwriter', options={'strings_to_urls': False})
        sample.to_excel(writer)
        writer.close()
        print('Workbook saved to ', self.full_path)



    def load_wb(self):
        wb = load_workbook(filename=self.full_path)
        return wb

    def write_wb(self, addr):
        msg = 'Writing from {ffrom} to {fto}'.format(ffrom=addr[0], fto=addr[1])
        print(msg)
        df = utils.load_shoes_dataset()
        sample = df.iloc[:self.samplesize]
        wb = self.load_wb()
        ws = wb.active
        processes = processing.img_pre_multiprocess(sample, ws, self.full_path)

        selection = []
        writings = []

        for i in range(addr[0], addr[1]+1):
            cellname = 'S{fnum}'.format(fnum=i)
            selection.append(cellname)

        for cell in selection:
            for i in range(0, len(processes)):
                if cell == processes[i][0]:
                    writings.append(processes[i])


        processing.img_processor_local(writings)

        print('XLSX processed successfully')

        return True

    def write_wb_xl(self, addr, iny_size=10):
        msg = 'Writing from {ffrom} to {fto}'.format(ffrom=addr[0], fto=addr[1])
        print(msg)
        df = utils.load_shoes_dataset()
        sample = df.iloc[:self.samplesize]
        wb = self.load_wb()
        ws = wb.active
        processes = processing.img_pre_multiprocess(sample, ws, self.full_path)

        selection = []
        writings = []

        for i in range(addr[0], addr[1]+1):
            cellname = 'S{fnum}'.format(fnum=i)
            selection.append(cellname)

        for cell in selection:
            for i in range(0, len(processes)):
                if cell == processes[i][0]:
                    writings.append(processes[i])

        processing.img_processor_local_inj(writings, iny_size)

        print('XLSX processed successfully')

        return True

    # CONNECTS TO CORE
    def update_prices(self):

        wb = self.load_wb()
        ws = wb.active

        # iterate through excel and display data
        # iterate through excel and display data
        for i in range(0, self.samplesize):

            price_cell = 'C{fnum}'.format(fnum=i+2)
            id_cell = 'E{fnum}'.format(fnum=i + 2)

            id = ws[id_cell]
            sneaker = core.get_shoe_by_id(id)
            try:
                new_price = sneaker[0]['estimatedMarketValue']
            except IndexError:
                continue
            ws[price_cell] = new_price

        wb.save(self.full_path)
        try:
            wb.save(self.full_path)
        except PermissionError:
            print('It seems like the xlsx is being used by another program, please close it first and try again.')

        print('Prices Updated Succesufully')
        return True















