"""

Prisma Inc.

handler.py

Status: UNDER DEVELOPMENT for Major Update Ryzen

Made by Alexis W.

"""



from sneakers.api.users import userbase
from sneakers.api.low import database
from sneakers.api.low import builder
import pandas as pd

import random

#------------------

# Ryzen Connection


def get_user_sneakers_ryzen(ids):

    users = userbase.load_userbase()

    userobj = users.loc[users['id'] == ids]

    currentportfolio = userobj['portfolio'].apply(eval)

    newport = currentportfolio.values[0]

    data = database.load_database_ryzen()

    newdata = data[0:0]

    for sneaker in newport:

        userobj = data.loc[data['sku'] == sneaker]

        newdata = newdata.append(userobj)


    dnewdata = newdata.drop_duplicates()

    userdatajson = builder.build_userdataset_ryzen(dnewdata)

    return userdatajson







#----------------


def user_login(email, password):

    users = userbase.load_userbase()

    userobj = users.loc[users['email'] == email]

    exist = len(userobj)

    if exist != 0:
        userobjpass = userobj['password'].values
        if userobjpass == password:
            uname = userobj['name'].values
            print('Welcome, {fname}'.format(fname=uname[0]))
            return userobj, True
        else:
            return 'Wrong Password', False

    else:
        return 'User does not exist', False

def user_signup(name, lastname, password, email):

    try:
        ids = random.randint(10000, 99999)

        print(ids)

        userdf = {'id': ids, 'name': name, 'lastname': lastname, 'password': password, 'email': email, 'sub': 0,
                  'portfolio': ['empty'], 'payment': 0}

        print(userdf)

        users = userbase.load_userbase()

        emailsq = users['email']



        emails = emailsq.to_list()

        print(emails)

        if email in emails:
            return 'User Already Registered'
        else:

            print(users)

            users = users.append(userdf, ignore_index=True)

            print(users)

            userbase.save_userdatabase(users)

            return(ids)

    except Exception as e:
        return('Something goes bad')



def user_addsneaker(ids, sneakersku):

    users = userbase.load_userbase()

    userobj = users.loc[users['id'] == ids]

    currentportfolio = userobj['portfolio'].apply(eval)

    newport = currentportfolio.values[0]

    for things in newport:
        if things == sneakersku:
            print('Sneaker already added')
            return False

    newport.append(sneakersku)

    currentportfolio['portfolio'] = newport

    userobj['portfolio'] = currentportfolio

    users.update(userobj)


    userbase.save_userdatabase(users)

    return True

def get_username(ids):

    users = userbase.load_userbase()

    userobj = users.loc[users['id'] == ids]

    usersname = userobj['name']

    return usersname


def get_user_sneakers(ids):

    users = userbase.load_userbase()

    userobj = users.loc[users['id'] == ids]

    currentportfolio = userobj['portfolio'].apply(eval)

    newport = currentportfolio.values[0]

    data = database.load_database()

    newdata = data[0:0]

    for sneaker in newport:

        userobj = data.loc[data['sku'] == sneaker]

        newdata = newdata.append(userobj)


    dnewdata = newdata.drop_duplicates()

    userdatajson = builder.build_userdataset(dnewdata)

    return userdatajson


def delete_duplicates(x):
  return list(dict.fromkeys(x))


def get_user_sneaker_list(ids):

    users = userbase.load_userbase()

    userobj = users.loc[users['id'] == ids]

    currentportfolio = userobj['portfolio'].apply(eval)

    newport = currentportfolio.values[0]

    return newport


def validate_sneaker(ssid, name):

    sneaker = database.get_sneaker_by_name(name)

    sku = sneaker['sku'].values[0]

    userlist = get_user_sneaker_list(int(ssid))

    for item in userlist:
        if item == sku:
            print('Validated Token')
            return True

        else:
            continue
    return False


def delete_sneaker(ids, sneakersku):

    users = userbase.load_userbase()

    userobj = users.loc[users['id'] == ids]

    currentportfolio = userobj['portfolio'].apply(eval)

    newport = currentportfolio.values[0]

    for things in newport:

        # print(things)

        if things == sneakersku:

            newport.remove(sneakersku)

            currentportfolio['portfolio'] = newport

            userobj['portfolio'] = currentportfolio

            users.update(userobj)

            userbase.save_userdatabase(users)

            print('Sneaker Deleted!')

            return False

        else:

            print('Sneaker does not exist')

    return True