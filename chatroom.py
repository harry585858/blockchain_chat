from db import User, Chatroom
from hash import sha512_hash
import json
from app import db
def verify(id, count,chats, people):
    if(id and count and chats and people):
        chatsjson = json.loads(chats)
        first_hash = chatsjson[0]
        last_hash = first_hash
        for i in chatsjson[1:]:
            last_hash = sha512_hash(last_hash+i)
        room = Chatroom.query.filter_by(id=id, first=first_hash ,last = last_hash, people=people, count=count).first()
        if(room == None):
            return False
        else:
            return room

    else:
        return False
def verify_enter(id, count,chats, people):
    room = verify(id, count,chats, people)
    if room == True:
        return room.temp

    else:
        return False
def new_msg(id, count, chats, people, msg):
    room = verify(id, count,chats, people)
    if room == True:
        room.temp = room.temp+id+':'+room.temp+';'
        db.session.commit()
