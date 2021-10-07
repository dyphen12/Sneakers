# Made by @dyphen12

from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import json
import os


from sneakers.api.composer import Composer
from sneakers.api.airtable_composer import Aircomposer
from sneakers.api.core import load_config
from sneakers.api.core import update_shoes_db
from sneakers.api.core import api_version
from sneakers.api.low import builder
from sneakers.api.users import handler as uhd


app = Flask(__name__)
api = Api(app)
CORS(app)

class Hello(Resource):

    def get(self):
        return api_version()


################# Deployment Api #######################

todos = {}


class InitWorkbook(Resource):

    def get(self, todo_id):
        xc = Composer(todo_id)
        return 'yay'


class expandWorkbook(Resource):

    def get(self, todo_id):
        print(todo_id)
        query = json.loads(todo_id)
        tit = query['results']['title']
        siz = query['results']['size']

        if tit == 'title':
            return 'Empty Title :('
        else:
            xc = Composer(tit)
            xc.expand_worksheet(siz)
            return 'yay'


class imagingWorkbook(Resource):

    def get(self, todo_id):
        print(todo_id)
        query = json.loads(todo_id)
        tit = query['results']['title']
        afrom = query['results']['from']
        ato = query['results']['to']
        listadd = [afrom, ato]

        if tit == 'title':
            return 'Empty Title :('
        else:
            xc = Composer(tit)
            cf = load_config()
            xc.write_wb_xl(listadd, cf.inysize)
            return 'yay'


class driveWorkbook(Resource):

    def get(self, todo_id):

        print(todo_id)
        try:
            global a
            tit = todo_id
            xc = Composer(tit)
            url, a = xc.drive_flow_gui()

            return url
        except TypeError:
            return 'Whoops'


class syncWorkbook(Resource):

    def get(self, todo_id):
        todo_2 = todo_id.replace('totona','/')
        print(todo_2)
        query = json.loads(todo_2)
        tit = query['results']['title']
        cod = query['results']['code']
        print(cod)
        print(type(a))


        if tit == 'title':
            return 'Empty Title :('
        else:
            xc = Composer(tit)
            xc.sync_worksheet(a, cod)
            return 'yay'


class infoWorkbook(Resource):

    def get(self, todo_id):
        xc = Composer(todo_id)

        data = {
    "composer": {
        "doc_id": xc.doc_id,
        "title": xc.title,
        "doc_name":xc.doc_file,
        "synced": xc.online,
        "size": xc.samplesize
    }}

        return data


class updateWorkbook(Resource):

    def get(self, todo_id):
        xc = Composer(todo_id)
        xc.update_prices()

        return 'Prices updated'

class updateDB(Resource):

    def get(self, todo_id):
        #xc = Composer(todo_id)
        print('Please, active the updates')
        #update_shoes_db()

        return 'Prices updated'

api.add_resource(Hello, '/')

api.add_resource(InitWorkbook, '/init/<string:todo_id>')
api.add_resource(expandWorkbook, '/expand/<string:todo_id>')
api.add_resource(imagingWorkbook, '/imaging/<string:todo_id>')
api.add_resource(driveWorkbook, '/drive/<string:todo_id>')
api.add_resource(syncWorkbook, '/sync/<string:todo_id>')
api.add_resource(infoWorkbook, '/info/<string:todo_id>')
api.add_resource(updateWorkbook, '/update/<string:todo_id>')
api.add_resource(updateDB, '/updatedb/<string:todo_id>')

#----------Airtable API----------

class InitTable(Resource):

    def get(self, todo_id):
        xc = Aircomposer(todo_id)
        return 'yay'

class InfoTable(Resource):

    def get(self, todo_id):
        xc = Aircomposer(todo_id)

        data = {
    "composer": {
        "doc_id": xc.doc_id,
        "title": xc.title,
        "doc_name":xc.doc_file,
        "synced": xc.online,
        "size": xc.samplesize
    }}

        return data

class DeployTable(Resource):

    def get(self, todo_id):
        print(todo_id)
        query = json.loads(todo_id)
        tit = query['results']['title']
        siz = query['results']['size']

        if tit == 'title':
            return 'Empty Title :('
        else:
            xc = Aircomposer(tit)
            r = xc.deploy_airtable(siz)
            if r is False:
                return 'Table already deployed...'
            else:
                return 'yay'


class updateTable(Resource):

    def get(self, todo_id):
        xc = Aircomposer(todo_id)
        xc.update_marketvalue()

        return 'Prices updated'

api.add_resource(InfoTable, '/infotable/<string:todo_id>')
api.add_resource(InitTable, '/inittable/<string:todo_id>')
api.add_resource(DeployTable, '/deploytable/<string:todo_id>')
api.add_resource(updateTable, '/updatetable/<string:todo_id>')


################# Ryzen Api #######################

class AllData(Resource):

    def get(self):
        x = builder.build_dataset_ryzen()
        return x


class AllDataIndexed(Resource):

    def get(self, todo_id):
        page = int(todo_id)
        x = builder.build_dataset_pages_ryzen(page)
        return x

api.add_resource(AllData, '/alldata')
api.add_resource(AllDataIndexed, '/alldataindex/<string:todo_id>')




################# Login Api #######################

CREDENTIAL = {
    'token1':{'user': "admin",
              'pass': "admin1"}
}

def abort_if_credential_doesnt_exist(token_id):
    if token_id not in CREDENTIAL:
        abort(404, message="Token {} doesn't exist".format(token_id))


parserauth = reqparse.RequestParser()
parserauth.add_argument('user')
parserauth.add_argument('pass')


class Login(Resource):

    def post(self):

        args = parserauth.parse_args()
        token_id = int(max(CREDENTIAL.keys()).lstrip('token')) + 1
        token_id = 'token%i' % token_id
        CREDENTIAL[token_id] = {'user': args['user'],
                                'pass': args['pass']}

        token = CREDENTIAL[token_id]

        x, auth = uhd.user_login_ryzen(token['user'],token['pass'])

        try:

            ids = x['id'].values[0]



            ssid = ids
            #print('auth success')

            return int(ssid)


        except TypeError:
            ids = 0
            print('auth failed')
            return 'fail'


api.add_resource(Login, '/auth')


class sneakerSaver(Resource):

    def get(self, todo_id):
        query = json.loads(todo_id)
        ids = query['results']['ssid']
        sku = query['results']['sku']

        uhd.user_addsneaker_ryzen(int(ids), str(sku))
        return 'yay'

api.add_resource(sneakerSaver, '/savethis/<string:todo_id>')


class getuserName(Resource):

    def get(self, todo_id):

        x = uhd.get_username_ryzen(int(todo_id))

        return x.values[0]


api.add_resource(getuserName, '/user/<string:todo_id>')


class userData(Resource):

    def get(self, todo_id):

        x = uhd.get_user_sneakers_ryzen(int(todo_id))

        if x is False:
            return 'fail'
        else:
            return x

api.add_resource(userData, '/userdata/<string:todo_id>')


class sneakerDeleter(Resource):

    def get(self, todo_id):
        query = json.loads(todo_id)
        ids = query['results']['ssid']
        sku = query['results']['sku']

        uhd.delete_sneaker_ryzen(int(ids), str(sku))
        return 'yay'

api.add_resource(sneakerDeleter, '/deletethis/<string:todo_id>')

class SignUp(Resource):

    def get(self, todo_id):
        query = json.loads(todo_id)
        uname = query['results']['name']
        ulastname = query['results']['lastname']
        uemail = query['results']['email']
        upass = query['results']['password']
        resulta = uhd.user_signup_ryzen(uname, ulastname, upass, uemail)

        return resulta


api.add_resource(SignUp, '/signup/<string:todo_id>')



class searchData(Resource):

    def get(self, todo_id):

        x = builder.build_search_ryzen(todo_id)

        if x is False:
            return 'fail'
        else:
            return x

api.add_resource(searchData, '/search/<string:todo_id>')


if __name__ == '__main__':
#    #app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
    app.run()