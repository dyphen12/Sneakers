"""

Prisma Inc. 2021

unit-test.py

Status: Checked

Note: For unit testing purposes.

Made by Alexis W.

"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sneakers.api.utils as skutils
from sneakers.api.composer import Composer
from sneakers.api.airtable_composer import Aircomposer
import sneakers.api.core as skcore
import sneakers.api.ticker as skticker
import sneakers.api.datautils as skdata
from sneakers.vision import dataset as skvdataset

titl = skutils.composer_title('composer', 'HelloWorld')

url = "https://goat.com/sneakers/lebron-18-ep-goat-cq9284-008"

if __name__ == '__main__':
    conf = skcore.load_config()
    data = skutils.load_shoes_dataset_quantity(5)
    skvdataset.build_training(data, 'dev')















    
    