from db import db
from models import User, Chatroom
from hash import sha512_hash
def join_user(id, pw):
    account = User.query.filter_by(
        id=id
    ).first()
    if account:
        return "ID Already exist", 400
    else:
        account = User(id=id,pw=sha512_hash(pw))
        db.session.add(account)
        db.session.commit()
        return id, 200
def delete_user(id, pw):
    account = User.query.filter_by(id=id).first()
    if not account:
        return "ID Not exist", 400

    # 비밀번호 검증 (sha512_hash로 해시한 값 비교)
    if account.pw != sha512_hash(pw):
        return "Invalid password", 403

    # 계정 삭제
    db.session.delete(account)
    db.session.commit()
    return f"User {id} deleted", 200