from flask import Flask, request
from chatroom import verify_enter, new_msg
app = Flask(__name__)

@app.route('/enter', methods=['POST'])
def enter():
    id = request.form.get('id')
    count = request.form.get('count')
    chats =request.form.get('chats')
    people = request.form.get('people')
    return verify_enter(id, count, chats, people)

@app.route('/message', methods=['POST'])
def message():
    id = request.form.get('id')
    count = request.form.get('count')
    chats =request.form.get('chats')
    people = request.form.get('people')
    msg = request.form.get('msg')
    return new_msg(id, count, chats, people, msg)

if __name__ == '__main__':
    app.run(debug=True)
