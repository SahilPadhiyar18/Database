import email
from unicodedata import name
from click import password_option
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json


app = Flask(__name__)

db = SQLAlchemy()
DB_NAME = "database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

class Logindata(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(1000))
    passsword = db.Column(db.String(1000))
    addkey = db.Column(db.String(1000))

    
@app.route('/', methods=['GET', 'POST']) 
def data():
    try:
        dates = db.session.query(Logindata.name).all()
        times = db.session.query(Logindata.email).all() 
        state = db.session.query(Logindata.passsword).all() 
        return render_template('data.html',data = dates[::-1] ,data1 = times[::-1],status = state[::-1])
    except:
        return "Error"
        
@app.route('/espupdate', methods=['GET','POST'])
def espupdate():
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        c = request.args.get('c')
        d = request.args.get('d')
        t = Logindata(name  = a , email= b ,passsword=c, addkey = d)
        db.session.add(t)
        db.session.commit()
        return "add done"
    except:
        return "pass"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # db.switch.drop()
    app.run(host='0.0.0.0', port=82)