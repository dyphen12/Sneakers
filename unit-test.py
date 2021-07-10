"""

Made by Alexis Wong.
Prisma Inc.

"""
import sneakers.api.core as sk
import sneakers.api.utils as skutils
import sneakers.api.uploaders as up
from datetime import datetime

now = datetime.now()

nowstr = now.strftime("%d-%m-%Y %H-%M-%S")



#skutils.flush_sheets()

shuset = skutils.load_shoes_dataset()

sample = shuset.iloc[:50]

#sample = shuset

slen = len(sample)

ver = 'DEBUGv2(building-big)-({flen}rows)-{ftime}'.format(ftime=nowstr, flen=slen)

if __name__ == '__main__':
    skutils.build_large_xlsx(sample, ver)
