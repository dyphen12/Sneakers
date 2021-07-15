# Made by @dyphen12

from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import json


from sneakers.api.composer import Composer

app = Flask(__name__)
api = Api(app)
CORS(app)

################# Deployment Api #######################

todos = {}

global a

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
            xc.write_wb_xl(listadd, iny_size=50)
            return 'yay'

class syncWorkbook(Resource):

    def get(self, todo_id):
        print(todo_id)
        query = json.loads(todo_id)
        tit = query['results']['title']

        if tit == 'title':
            return 'Empty Title :('
        else:
            xc = Composer(tit)
            url, a = xc.sync_flow_gui()
            return url

class sync2Workbook(Resource):

    def get(self, todo_id):
        print(todo_id)
        query = json.loads(todo_id)
        tit = query['results']['title']
        cod = query['results']['code']

        if tit == 'title':
            return 'Empty Title :('
        else:
            xc = Composer(tit)
            xc.sync_flow_gui_code(cod, a)
            return 'yay'



api.add_resource(InitWorkbook, '/init/<string:todo_id>')
api.add_resource(expandWorkbook, '/expand/<string:todo_id>')
api.add_resource(imagingWorkbook, '/imaging/<string:todo_id>')
api.add_resource(syncWorkbook, '/sync/<string:todo_id>')
api.add_resource(sync2Workbook, '/sync2/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)