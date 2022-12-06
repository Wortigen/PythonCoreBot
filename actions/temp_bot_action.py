def StartBotAction():
    global varObj
    core = varObj.get('core')
    botSchema = None
    for schema in core.schema:
        if schema.ShowName() == 'tBot' or schema.ShowType() == 'bot':
            botSchema = schema.GetActions()
    tBot = TelegramBot('5873286537:AAGIkmamsETS4esUdMOHX5ZZbIcrrFRtT2k')
    tBot.Events = botSchema
    if 'tBot_chats' in varObj.temp.keys():
        if bool(varObj.temp['tBot_chats']):
            tBot.chats = varObj.temp['tBot_chats']
        del varObj.temp['tBot_chats']
    if 'tBot_user' in varObj.temp.keys():
        if bool(varObj.temp['tBot_user']):
            tBot.users = varObj.temp['tBot_user']
        del varObj.temp['tBot_user']
    del botSchema
    varObj.save('tBot', tBot)
    tBot.Run()
