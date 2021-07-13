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
import sneakers.api.uploaders as up
from datetime import datetime

# Get current datetime
now = datetime.now()

# Change the date format
nowstr = now.strftime("%d-%m-%Y %H-%M-%S")

# Loads the database
shuset = skutils.load_shoes_dataset()

# Pick a sample from the dataset
sp = 100  # Sample Size
sample = shuset.iloc[:sp]

# Get length from sample
slen = len(sample)

# Set up the title for the xlsx
ver = 'CLOUD(computing-perfomance)-({flen}rows)-{ftime}'.format(ftime=nowstr, flen=slen)

if __name__ == '__main__':

    #skutils.download_img(sample)
    #skutils.build_big_xlsx(sample, ver, local=True)

    # Build XLSX with the Injector
    skutils.build_xlxs_injector(sample, ver, size=3, local=False)

