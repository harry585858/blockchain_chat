import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
conn = sqlite3.connect('mydata.db')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Chatroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer) #how long
    first = db.Column(db.String) #16digit hash
    last = db.Column(db.String)
    people = db.Column(db.String)
    temp = db.Column(db.String) #json data