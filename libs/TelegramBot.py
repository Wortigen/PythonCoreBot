class TelegramBot:
    tBot = None
    token = None

    def __init__(self, token):
        self.token = token
        self.tBot = telebot.TeleBot(token)
        self.chats = dict()
        self.users = dict()
        self.connect = dict()
        self.Events = None

    def Run(self, once = False):
        global varObj
        tBot_comm = varObj.get('tBot_config')
        @self.tBot.message_handler(commands=tBot_comm['commands'])
        def _process_comand_start(msg):
            #print("New request command:=>", msg.text)
            #print("Request chat :=>", msg.chat.id)
            #print("Request user :=>", msg.from_user.id)
            self.process_comand_start(msg)

        @self.tBot.message_handler()
        def _process_message_start(msg):
            #print("New request text:=>", msg.text)
            #print("Request chat :=>", msg.chat.id)
            #print("Request user :=>", msg.from_user.id)
            self.process_message_start(msg)

        @self.tBot.message_handler(func=self.callback_worker, content_types=['document'])
        def _callback_worker(call):
            #print("New request file :=>", msg.text)
            #print("Request chat :=>", msg.chat.id)
            #print("Request user :=>", msg.from_user.id)
            self.callback_worker(call)

        if once == False:
            self.tBot.polling(none_stop=True)


    def callback_worker(self, data):
        key = 'U' + str(data.from_user.id) + 'C' + str(data.chat.id)
        if not key in self.connect:
            self.connect[key] = {'user': data.from_user.id, 'chat': data.chat.id}
        chat = self.checkChats(data.chat)
        user = self.checkUser(data.from_user)
        if self.CheckUserForChat(user,chat) == True:
            self.CheckEventsState('send_file', self.PreperTempData(data, 'file'))
        self.EndConnection(key)

    def process_comand_start(self,message):
        key = 'U' + str(message.from_user.id) + 'C' + str(message.chat.id)
        if not key in self.connect:
            self.connect[key] = {'user': message.from_user.id, 'chat': message.chat.id}
        chat = self.checkChats(message.chat)
        user = self.checkUser(message.from_user)
        if self.CheckUserForChat(user,chat) == True:
            self.CheckEventsState('write_command', self.PreperTempData(message, 'mess'))
        self.EndConnection(key)

    def process_message_start(self, message):
        key = 'U' + str(message.from_user.id) + 'C' + str(message.chat.id)
        if not key in self.connect:
            self.connect[key] = {'user': message.from_user.id, 'chat': message.chat.id}
        chat = self.checkChats(message.chat)
        user = self.checkUser(message.from_user)
        if self.CheckUserForChat(user,chat) == True:
            self.CheckEventsState('write_text', self.PreperTempData(message, 'mess'))
        self.EndConnection(key)

    def answer_from_bot(self, chat_id = 0, msg = ''):
        self.tBot.send_message(chat_id,msg)

    def answer_from_bot_file(self, chat_id, path, type):
        file = FileWorker()
        if file.isExist(path):
            match type:
                case 'doc':
                    fileByte = file.ReadFileByte(path)
                    self.tBot.send_document(chat_id, fileByte)

    def get_file(self, id):
        return self.tBot.get_file(id)

    def download_file(self, path):
        return self.tBot.download_file(path)

    def checkChats(self, chat):
        if chat.id in self.chats.keys():
            pass
        else:
            self.chats[chat.id] = ChatObj()
            self.chats[chat.id].NewChat(chat)
            self.CheckEventsState('append_chat', self.PreperTempData(self.chats[chat.id], 'chat'))
        return self.chats[chat.id].GetChatArgs()

    def checkUser(self, user):
        if user.id in self.users.keys():
            pass
        else:
            self.users[user.id] = UserObj()
            self.users[user.id].NewUser(user)
            self.CheckEventsState('new_user', self.PreperTempData(self.users[user.id], 'user'))
        return self.users[user.id].GetUserArgs()

    def CheckUserForChat(self,user,chat):
        self.CheckEventsState('check_chat_user', self.PreperTempData({'user': user, 'chat': chat},'chat_user'))
        return True

    def CheckEventsState(self, event = '', key = ''):
        res = None
        act = None
        if self.Events != None:
            for ev in self.Events:
                if ev['event'] == event:
                    #print(f"Run event :=> {event}")
                    ev['keyData'] = key
                    act = ActivatorAction()
                    act.add(ev)

        if act != None:
            act.Run()
        return res

    def PreperTempData(self, obj, type):
        global varObj
        key = None
        if type == 'user':
            key = 'U' + str(obj.id)
            varObj.temp[key] = obj
        if type == 'chat':
            key = 'C' + str(obj.id)
            varObj.temp[key] = obj
        if type == 'chat_user':
            key = 'C' + str(obj['chat']['id']) + 'U' + str(obj['user']['id'])
            varObj.temp[key] = obj
        if type == 'mess':
            key = 'm' + str(obj.id)
            varObj.temp[key] = obj
        if type == 'file':
            key = 'f' + str(obj.id)
            varObj.temp[key] = obj

        return key

    def EndConnection(self, key):
        print("Clear session :=>", self.connect[key])
        if not 'act' in self.connect[key].keys():
            print("Must don't delete ==============")
            del self.connect[key]
