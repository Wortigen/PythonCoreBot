def bot_new_user(key = None):
    global varObj
    tBot = varObj.get('tBot')
    print("Add new User")

    temp_data = varObj.temp[key]
    del varObj.temp[key]

    user = tBot.users[temp_data.id]

    tBot_config = varObj.get('tBot_config')
    tBot_config = tBot_config['wait_user']

    if user.username in tBot_config.keys():
        user.status = tBot_config[user.username]['status']
        user.position = tBot_config[user.username]['position']
        user.permission = tBot_config[user.username]['permission']
        mess = ''
        if user.username == "klebanyaroslav":
            mess = "привіт, я бот який тепер стежитиме за своїми доменами))\n\n"
            mess +="І я знав, що ти прийдеш до мене!!!\n"
            mess +=f"Тепер твій статус: {user.status}\n Твоя позиція: {user.position}\n"
            mess +="зможеш піднятись чи ні буде судити час\n"
            mess +="Дізнатися про можливості можна за допомогою заклинання: /help"
        else:
            mess = "привет, я бот который теперь будет слидеть за своими доменами))\n\n"
            mess +="И я знал что ты придешь ко мне!!!\n"
            mess +=f"Теперь твой статус: {user.status}\n Твоя позиция: {user.position}\n"
            if user.username == "serhiiredko":
                mess +="как покорение всех индусов с возможностью на деп?\n"
                mess +="если че начинай общение с /help а там разберемся чем могу помочь"
            else:
                mess +="сможеш поднятся или нет будет судить время\n"
                mess +="Узнать о возможностях можно с помощью заклинания: /help"

        list_connect = tBot.connect.keys()
        find_connect = list()
        for x in list_connect:
            if tBot.connect[x]['user'] == user.id:
                find_connect.append(tBot.connect[x])

        print("Find connects :=>", find_connect)
        if len(find_connect) == 1:
            print("Find connect :=>", find_connect[0]['chat'])
            tBot.answer_from_bot(find_connect[0]['chat'], mess)
        else:
            for con in find_connect:
                chat = tBot.chats[con['chat']]
                if chat.type == 'private':
                    tBot.answer_from_bot(chat.id, mess)
                else:
                    print(f"Some error with answer from user :=> {user.username} ; id user :=> {user.id}")
