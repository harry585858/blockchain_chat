import os
from flask import Flask, request
from db import db
from models import User, Chatroom
from chatroom import verify_enter, new_msg, new_room
from accounts import join_user, delete_user
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/enter', methods=['POST'])
def enter():
    id: str = request.form.get('id')
    roomid = request.form.get('roomid')
    count = request.form.get('count')
    chats: str =request.form.get('chats')
    people = request.form.get('people')
    return verify_enter(id,roomid, count, chats, people)

@app.route('/message', methods=['POST'])
def message():
    id = request.form.get('id')
    roomid = request.form.get('roomid')
    count = request.form.get('count')
    chats =request.form.get('chats')
    people = request.form.get('people')
    msg = request.form.get('msg')
    return new_msg(id, roomid, count, chats, people, msg)

@app.route('/createroom', methods=['POST'])
def createroom(id: str, people):
    id = request.form.get('id')
    people = request.form.get('people')
    if new_room(id, people):
        return id
    else:
        return "You are not included", 400

@app.route('/join', methods=['POST'])
def join():
    id = request.form.get('id')
    pw = request.form.get('pw')
    if id and pw:
        return join_user(id,pw)
    return "Fill it all", 400

@app.route('/delete-account', methods=['DELETE'])
def delete():
    id = request.form.get('id')
    pw = request.form.get('pw')
    if id and pw:
        return delete_user(id,pw)
    return "Fill it all", 400


if __name__ == '__main__':
    app.run(debug=True)
