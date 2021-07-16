# Made by @dyphen12

from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import json
import os


from sneakers.api.composer import Composer
from sneakers.api.core import load_config
from sneakers.api.core import update_shoes_db

app = Flask(__name__)
api = Api(app)
CORS(app)

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

api.add_resource(InitWorkbook, '/init/<string:todo_id>')
api.add_resource(expandWorkbook, '/expand/<string:todo_id>')
api.add_resource(imagingWorkbook, '/imaging/<string:todo_id>')
api.add_resource(driveWorkbook, '/drive/<string:todo_id>')
api.add_resource(syncWorkbook, '/sync/<string:todo_id>')
api.add_resource(infoWorkbook, '/info/<string:todo_id>')
api.add_resource(updateWorkbook, '/update/<string:todo_id>')
api.add_resource(updateDB, '/updatedb/<string:todo_id>')

#if __name__ == '__main__':
#    #app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
#    app.run(debug=True)