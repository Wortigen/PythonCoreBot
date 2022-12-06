def bot_write_text(key = None):
    global varObj
    tBot = varObj.get('tBot')
    tBot_config = varObj.get('tBot_config')
    temp_data = varObj.temp[key]
    del varObj.temp[key]


    comm = temp_data.text
    chat = tBot.chats[temp_data.chat.id]
    user = tBot.users[temp_data.from_user.id]
    isIgnore = chat.isIgnore
    isDo = True
    mess = ''

    if not temp_data.text in tBot_config['commands']:
        con = None
        list_keys_connection = tBot.connect.keys()
        for x in list_keys_connection:
            if tBot.connect[x]['user'] == temp_data.from_user.id and tBot.connect[x]['chat'] == temp_data.chat.id:
                con = tBot.connect[x]

        if 'action' in con.keys():
            pass
        else:
            if tBot.chats[con['chat']].type == 'private':
                tBot.answer_from_bot(con['chat'], "I don't understand. try command /help for more detail")
            else:
                print("some wrong in action tBot write text")
