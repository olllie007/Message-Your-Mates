from flask import Flask, session
from flask_restful import Api, Resource
import sqlite3

conn = sqlite3.connect('message.db')
c = conn.cursor()


app = Flask(__name__)
api = Api(app)

class person1(Resource):
    def get(self, text, person, name):
        try:
            conn = sqlite3.connect('messaged.db')
            c = conn.cursor()
            sql = "SELECT * FROM " + name
            c.execute(sql)
            items = c.fetchall()
            length = len(items)
            length = length - 1
            item = items[length][0]
            print(item)
            return {'message': item}
        except:
            create =  'CREATE TABLE ' + name + ' (message text)'
            e.execute(create)
    def post(self, text, person, name):
        try:
            conn = sqlite3.connect('messaged.db')
            c = conn.cursor()
            sql = 'INSERT INTO ' + person + ' VALUES(?)'
            c.execute(sql, [text])
            conn.commit()
        except:
            no_one = 'No one with the Username ' + person
            conn.commit
            return no_one

    
api.add_resource(person1, '/person1/<string:text>/<string:person>/<string:name>')
if __name__  == "__main__":
    app.run(use_reloader=False, debug=False)
