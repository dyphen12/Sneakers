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


titl = skutils.composer_title('composer', 'HelloWorld')

if __name__ == '__main__':
    xc = Composer(titl)
    xc.expand_worksheet(100)
    xc.write_wb([2,10])









    
    