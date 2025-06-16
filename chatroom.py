from db import db
from hash import sha512_hash
from models import User, Chatroom
import json

# 유효성 검사
def verify(id, roomid, count, chats, people):
    if id and roomid and count and chats and people:
        chatsjson = json.loads(chats)

        # 해시 계산: 처음은 첫 메시지 그대로
        first_hash = chatsjson[0]
        last_hash = first_hash
        for i in chatsjson[1:]:
            last_hash = sha512_hash(last_hash + i)  # 안전한 해시 계산

        # 룸 검색
        room = Chatroom.query.filter_by(
            roomid=roomid,
            first=first_hash,
            last=last_hash,
            people=people,
            count=count
        ).first()

        if room is None:
            return False

        peoplejson = json.loads(room.people)
        if id in peoplejson:
            return room
        return False
    else:
        return False

# 입장 시 검증
def verify_enter(id, roomid, count, chats, people):
    room = verify(id, roomid, count, chats, people)
    if room:
        return room.temp
    else:
        return False

# 메시지 저장
def new_msg(id, roomid, count, chats, people, msg):
    room = verify(id, roomid, count, chats, people)
    if room:
        room.temp += f"{id}:{msg},"
        room.last = sha512_hash(room.last + msg)  # 안전하게 해시 업데이트
        db.session.commit()

# 새 방 생성
def new_room(id, people):
    room = Chatroom(
        id=id,
        people=people,
        count=0,
        first="",
        last="",
        temp=""
    )
    db.session.add(room)
    db.session.commit()