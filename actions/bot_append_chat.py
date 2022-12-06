def bot_append_chat(key = None):
    global varObj
    tBot = varObj.get('tBot')
    print("Add new chat")
    
    temp_data = varObj.temp[key]
    del varObj.temp[key]

    chat = tBot.chats[temp_data.id]

    if chat.type == 'group':
        chat.isIgnore = True

    tBot.chats[temp_data.id] = chat
