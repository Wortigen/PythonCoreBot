class UserObj:

    def __init__(self):
        self.id = -1
        self.name = ''
        self.surname = ''
        self.username = ''
        self.status = None
        self.position = ''
        self.permission = list()
        self.listChat = list()

    def NewUser(self, args = dict()):
        self.id = args.id
        self.name = args.first_name
        self.surname = args.last_name
        self.status = 'new user'
        self.username = args.username
        self.position = 'Guest'
        self.permission.append('guest')
        self.listChat = list()

    def AddChat(self, chat_id):
        self.listChat.append(chat_id)

    def GetUserArgs(self):
        temp = dict()
        temp['id'] = self.id
        temp['username'] = self.username
        temp['position'] = self.position
        temp['permission'] = self.permission
        temp['status'] = self.status
        return temp

    def ToSave(self):
        temp = dict()
        temp['id'] = self.id
        temp['name'] = self.name
        temp['surname'] = self.surname
        temp['username'] = self.username
        temp['status'] = self.status
        temp['position'] = self.position
        temp['permission'] = self.permission
        temp['listChat'] = self.listChat
        return temp

    def ToLoad(self, data):
        self.id = data['id']
        self.name = data['name']
        self.surname = data['surname']
        self.username = data['username']
        self.status = data['status']
        self.position = data['position']
        self.permission = data['permission']
        self.listChat = data['listChat']
