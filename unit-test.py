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

sample = shuset.iloc[:50000]

#sample = shuset

slen = len(sample)

ver = 'CLOUD(computing-perfomance)-({flen}rows)-{ftime}'.format(ftime=nowstr, flen=slen)

if __name__ == '__main__':
    #skutils.download_img(sample)
    #skutils.build_big_xlsx(sample, ver, local=True)
    skutils.build_xlxs_injector(sample, ver, size=100, local=False)

