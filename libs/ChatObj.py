class ChatObj:

    def __init__(self):
        self.id = 0
        self.type = None
        self.type_chat = None
        self.isIgnore = False
        self.blacklist = list()
        self.none_permission = list()
        self.ignore = list()
        self.Users = list()


    def NewChat(self, args = dict()):
        self.id = args.id
        self.type = args.type
        if args.type == 'private':
            self.type_chat = args.type

    def AddUser(self, user_id):
        self.Users.append(user_id)

    def GetChatArgs(self):
        temp = dict()
        temp['id'] = self.id
        temp['type'] = self.type
        temp['type_chat'] = self.type
        if self.type == 'group':
            temp['userList'] = self.Users
            temp['ignoreList'] = self.ignore
            temp['none_permission'] = self.none_permission
            temp['blackList'] = self.blacklist
        return temp

    def ToSave(self):
        temp = dict()
        temp['id'] = self.id
        temp['type'] = self.type
        temp['type_chat'] = self.type_chat
        temp['isIgnore'] = self.isIgnore
        temp['blacklist'] = self.blacklist
        temp['none_permission'] = self.none_permission
        temp['ignore'] = self.ignore
        temp['Users'] = self.Users
        return temp

    def ToLoad(self, temp):
        self.id = temp['id']
        self.type = temp['type']
        self.type_chat = temp['type_chat']
        self.isIgnore = temp['isIgnore']
        self.blacklist = temp['blacklist']
        self.none_permission = temp['none_permission']
        self.ignore = temp['ignore']
        self.Users = temp['Users']
