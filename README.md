# blockchain_chat

chat sevice with block chain

how to use api
```
  /enter
    id,roomid, count, chats, people
  /message
    id, roomid, count, chats, people, msg
  /createroom
    id,people
  /join
    id,pw
  /delete-account
    id,pw
```

detail
```
  people: string('id:id,')
  id: string
  count: int
  chats: string('id:msg,')