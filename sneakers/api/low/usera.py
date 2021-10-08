"""

Prisma Inc.

usera.py

Status: UNDER DEVELOPMENT for Major Update Ryzen

Made by Alexis W.

"""

import pandas as pd
import random

def load_usera():
    usera = pd.read_csv('sneakers/internal/usera.csv', index_col=1, low_memory=False)
    return usera

def getsome():

    useragents = load_usera()

    ualist = useragents['useragents']

    userix = ualist.to_list()

    x = random.choice(userix)

    return x