def bot_send_file(key = None):
    global varObj
    tBot = varObj.get('tBot')
    config = varObj.get('config')
    tBot_config = varObj.get('tBot_config')
    temp_data = varObj.temp[key]
    del varObj.temp[key]

    chat = tBot.chats[temp_data.chat.id]
    user = tBot.users[temp_data.from_user.id]
    key = 'U' + str(user.id) + 'C' + str(chat.id)
    conn = tBot.connect[key]
    isIgnore = chat.isIgnore
    isDefault = False
    isDo = True
    mess = ""

    if chat.type == 'group':
        if user.id in chat.blacklist:
            isDo = False
            mess = 'Вы в моем черном списке. \n'
            mess += 'Так что пожалуйста отвалите, просто ОТВАЛИТЕ!!!'

        if user.id in chat.ignore:
            isDo = False
            mess = 'Мы можем пообщатся но не тут. \n'
            mess += 'Я официально заявляю что буду игнорировать вас, но только здесь.\n'
            mess += 'Напомню что я непоколебим в этом вопросе)'

        if user.id in chat.none_permission:
            isDefault = True
            mess = 'Предупреждаю сдесь вы лиш гость.\n'
            mess += 'Такое к вам отношение будет в этом чате'

    if isIgnore == False and mess != '':
        tBot.answer_from_bot(chat.id, mess)
        mess = ''


    if 'weit' in conn.keys():
        if temp_data.document.mime_type == 'text/csv':
            file_info = tBot.get_file(temp_data.document.file_id)
            downloaded_file = tBot.download_file(file_info.file_path)
            File = FileWorker()
            File.CreateFileByContentByte(File.FolderCongig(), 'domainsTemp.csv', downloaded_file)
            del conn['act'], conn['weit']
            if varObj.isExistKey('update_domain') == False:
                updated = dict()
                updated[1] = File.FolderCongig() + '/domainsTemp.csv'
                varObj.save('update_domain', updated)
            else:
                updated = varObj.get('update_domain')
                ind = updated.keys()
                updated[len(ind)] = File.FolderCongig() + '/domainsTemp.csv'
                varObj.update('update_domain', updated)
            mess = "Файл загружен. Вас вернуло в корень комманд.\n их можно узнать через /help"
        else:
            mess = "не опознаное разширение файла."
    else:
        mess = "Сейчас не ожидается загрузки файла.\n"
        mess += "Возможно вы перепутали действия или команды.\n"
        mess += "Советую одуматся, пока не поздно"

    if isIgnore == False and mess != '':
        tBot.answer_from_bot(chat.id, mess)
        mess = ''

    varObj.update('tBot', tBot)
    del conn,user,chat
