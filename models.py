from db import db

class User(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    pw = db.Column(db.String(128))

class Chatroom(db.Model):
    roomid = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    first = db.Column(db.String(128))
    last = db.Column(db.String(128))
    people = db.Column(db.String(512))
    temp = db.Column(db.Text)