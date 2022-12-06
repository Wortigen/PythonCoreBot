def bot_write_command(key = None):
    global varObj
    tBot = varObj.get('tBot')
    config = varObj.get('config')
    tBot_config = varObj.get('tBot_config')
    temp_data = varObj.temp[key]
    del varObj.temp[key]

    comm = temp_data.text
    chat = tBot.chats[temp_data.chat.id]
    user = tBot.users[temp_data.from_user.id]
    key = 'U' + str(user.id) + 'C' + str(chat.id)
    conn = tBot.connect[key]
    isIgnore = chat.isIgnore
    isDefault = False
    isDo = True
    mess = ''

    def DoCommandLine(comm = ''):
        ans = ''
        match comm:
            case 'start':
                ans = 'Привет рад видеть у себя.\n Для более детального знакомстав используй /help'
            case 'help':
                ans = 'сейчас доступны такие команды:\n'
                ans += '/chat - команда раздела управления чата.\n'
                ans += '/files - раздел управления файлами.\n'
            case 'chat':
                ans = 'Вы вошли в раздел управление чатов.\n\n'
                ans += '/list_chat - список чатов\n'
                ans += '/edit_chat - редактировать чат\n\n'
                ans += '/back - вернутся назад.\n'
                ans += '/finish - Выйти в основной раздел команд.\n'
                if 'act' in conn.keys():
                    conn['act'].append(comm)
                else:
                    conn['act'] = list()
                    conn['act'].append(comm)
            case 'files':
                ans = 'Вы вошли в раздел управление чатов.\n\n'
                ans += '/empty_domains - файл пустой заготовки\n'
                ans += '/get_domains - Загрузить файл с доменами\n'
                ans += '/upload_domains - Загрузить список доменов\n\n'
                ans += '/back - вернутся назад.\n'
                ans += '/finish - Выйти в основной раздел команд.\n'
                if 'act' in conn.keys():
                    conn['act'].append(comm)
                else:
                    conn['act'] = list()
                    conn['act'].append(comm)
            case 'empty_domains':
                temp = DomainsObj()
                file = FileWorker()
                convert = Convertor()
                convert.Set(temp.GetStruct())
                convert.CSVHeaderConvert()
                file.path = config['temp_path'] + '/empty_domains.csv'
                file.content = list()
                file.content.append(convert.Get())
                file.FileWrite()
                tBot.answer_from_bot_file(chat.id, file.path, 'doc')
            case 'get_domains':
                tBot.answer_from_bot_file( chat.id, varObj.get('domainsFile'), 'doc')
            case 'upload_domains':
                if 'act' in conn.keys():
                    conn['act'].append(comm)
                    conn['weit'] = 'file'
                    ans = 'Загрузите файл со списком.\n Ожидается csv формат файла.'
            case 'back':
                if 'act' in conn.keys():
                    conn['act'].pop()
            case 'finish':
                if 'act' in conn.keys():
                    del conn['act']
            case _:
                ans = 'Такой комманды нет.\n Используйте спавку /help'

        tBot.connect[key] = conn
        return ans

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

    comm = comm[1:]

    if comm in tBot_config['commands']:
        canDo = False
        for permission in user.permission:
            if tBot_config['policy_structure'][permission]:
                check = tBot_config['policy_structure'][permission]
                if comm in check:
                    canDo = True
                if 'all' in check:
                    canDo = True
        if canDo == True:
            mess = DoCommandLine(comm)
        else:
            mess = "У вас не достаточно полномочий или веса в должности\n"
    else:
        mess = "Такие заклинания тут не пашут))\n"
        mess += "сколько не старайся только лишь дырку увеличешь от потуг\n\n"
        mess += "Хахахахаха"

    if isIgnore == False and mess != '':
        tBot.answer_from_bot(chat.id, mess)
        mess = ''

    varObj.update('tBot', tBot)
    del conn,user,chat,comm
