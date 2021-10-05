"""

Prisma Inc. 2021

unit-testmongo.py

Status: Checked

Note: For unit testing purposes.

Made by Alexis W.

"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from sneakers.api.low import database as lowd
from sneakers.api.low import builder as bd



if __name__ == '__main__':
    #lowd.load_database_ryzen()
    #bd.build_dataset_ryzen()
    print(bd.build_search_ryzen('adan smith swarovski'))