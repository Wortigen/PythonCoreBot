def bot_check_chat_user(key = None):
    global varObj
    tBot = varObj.get('tBot')

    temp_data_chat = varObj.temp[key]['chat']
    tempt_data_user = varObj.temp[key]['user']

    chat = tBot.chats[temp_data_chat['id']]
    user = tBot.users[tempt_data_user['id']]

    if not chat.id in user.listChat:
        user.listChat.append(chat.id)

    if not user.id in chat.Users:
        chat.Users.append(user.id)

    tBot.chats[temp_data_chat['id']] = chat
    tBot.users[tempt_data_user['id']] = user

    print("bot count chats :=>", len(tBot.chats))
    print("Bot count users :=>", len(tBot.users))

    File = FileWorker()

    file_content = dict()
    chat_keys = tBot.chats.keys()
    for ind in chat_keys:
        file_content[ind] = tBot.chats[ind].ToSave()
    File.path = varObj.get('chatFile')

    File.content = file_content
    File.type_content = 'json'
    File.RefreshFile()

    File.content = None
    File.type_content = None

    file_content = dict()
    user_keys = tBot.users.keys()
    for ind in user_keys:
        file_content[ind] = tBot.users[ind].ToSave()

    File.path = varObj.get('userFile')
    File.content = file_content
    File.type_content = 'json'
    File.RefreshFile()
