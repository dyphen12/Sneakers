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

import sneakers.api.core as sk
import sneakers.api.utils as skutils
from sneakers.api.composer import Composer
import sneakers.api.core as skcore


sp = 250  # Sample Size

titl = skutils.composer_title('composer', 'Cloud9Dev', sp)

if __name__ == '__main__':
    #skutils.download_img(sample)
    #skutils.build_big_xlsx(sample, ver, local=True)

    xcomposer = Composer(titl, samplesize=sp)
    #xcomposer.create_workbook()
    #xcomposer.update_prices()
    #xcomposer.write_wb([2,6])
    #xcomposer.sync_file()

    
    









