"""

Prisma Inc.

userbase.py

Status: UNDER DEVELOPMENT for Major Update Ryzen

Made by Alexis W.

"""

import pandas as pd



def save_userdatabase(df):
    df.to_csv('sneakers/api/users/usersdatabase.csv', index=False)
    print('Database has been modified and saved.')
    return True


def load_userbase():

    users = pd.read_csv('sneakers/api/users/usersdatabase.csv', low_memory=False)

    return users


