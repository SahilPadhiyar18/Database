import email
from unicodedata import name
from click import password_option
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import pymongo

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) 
def data():
    try:
        client = pymongo.MongoClient("mongodb+srv://SahilCluster18:meHtA9662@sahilcluster.qmaty.mongodb.net/?retryWrites=true&w=majority")
#        db = client.test 
#         client = pymongo.MongoClient("mongodb+srv://SahilCluster18:meHtA9662@sahilcluster.qmaty.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#         db = client.test
        db1 = client["tankdata"]
        dates = client.list_database_names()
        times = client.list_database_names() 
        state = client.list_database_names() 
        return "Done"
    except:
        return "Error"

@app.route('/espupdate', methods=['GET','POST'])
def espupdate():
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        c = request.args.get('c')
        d = request.args.get('d')
        # t = Logindata(name  = a , email= b ,passsword=c, addkey = d)
        # db.session.add(t)
        # db.session.commit()
        return "add done"
    except:
        return "pass"

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    # db.switch.drop()
    app.run()
