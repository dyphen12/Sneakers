"""

Prisma Inc. 2021

airtable_composer.py

Status: Checked

Note: For unit testing purposes.

Made by Alexis W.

"""
from sneakers.api import datautils
from sneakers.api import ticker

import pandas as pd

class Aircomposer:
    def __init__(self, title):
        self.exist = False
        self.samplesize = 5
        self.folder = 'airout'
        self.title = title
        self.doc_file = '{ftit}.csv'.format(ftit=title)
        self.full_path = 'airout/{ftit}.csv'.format(ftit=title)
        self.doc_id = 'Airtable ID not available.'
        self.online = False
        self.json_name = 'airout/{}.json'.format(title)
        self.datadoc = pd.DataFrame

        self.load_from_air()

    def deploy_airtable(self, size):
        if self.online is True:
            print('Table already deployed...')
            return False

        else:
            print('Deploying selected data into table {ftit}...'.format(ftit=self.title))
            datautils.to_airtable(self.title, size)
            self.samplesize = size
            self.online = True
            print('Succesfully Deployed!')
            return True

    def load_from_air(self):

        air_records = datautils.load_airtable(self.title)

        try:
            if air_records['error']['type'] == 'TABLE_NOT_FOUND':
                self.online = False
                print('Table not found in Airtable, may you wanna create it?')
                return True
        except TypeError:
            pass


        data = datautils.convert_to_dataframe(air_records)



        if data.empty is True:
            print('Table is either empty or does not have fields configured yet!')
            print('You want to deploy?')
            print('WARNING: Make sure you have the right fields in the table for loading it into the Composer')
            self.samplesize = 0
            self.online = False
        else:
            print('Woohoo, table of {flen} rows loaded!'.format(flen=len(data)))
            self.samplesize = len(data)
            self.online = True
            self.datadoc = data
            self.save_csv()

    def load_dataframe(self):

        air_records = datautils.load_airtable(self.title)

        try:
            if air_records['error']['type'] == 'TABLE_NOT_FOUND':
                self.online = False
                print('Table not found in Airtable, may you wanna create it?')
                return True
        except TypeError:
            pass


        data = datautils.convert_to_dataframe(air_records)


        if data.empty is True:
            self.samplesize = 0
            self.exist = False
            return 'Nada :('
        else:

            return data

    def save_csv(self):
        print('Syncing...')
        if self.exist is False:
            df = self.load_dataframe()
            df.to_csv(self.full_path)
            print('Table synced!')
            self.exist = True
        else:
            print('Already synced')

    def update_marketvalue(self):
        newpriceslist = []
        if self.online is True:
            current = self.datadoc
            for row in current.iterrows():
                # print(row[1]['link3'])
                # print(row[1]['estimatedMarketValue'])
                url = row[1]['link3']
                newprice = ticker.get_price_silence(url)
                if newprice is None:
                    print('Price scrap failed...')
                    newpriceslist.append(row[1]['estimatedMarketValue'])
                    continue
                else:
                    newpriceslist.append(newprice)


                # print(newprice)

            self.exist = False


            current['estimatedMarketValue'] = newpriceslist
            # print(current['estimatedMarketValue'])
            self.datadoc = current
            datautils.upload_airtable(self.title, current)
            self.save_csv()
            return current
        else:
            print('Table does not exist or is empty.')

        return True
