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


sp = 100  # Sample Size

titl = skutils.composer_title('composer', 'Danieleo1', sp)

if __name__ == '__main__':
    
    
    xcomposer = Composer(titl, samplesize=sp)
    
    xcomposer.write_wb_xl([5,20],iny_size=5)
    
    