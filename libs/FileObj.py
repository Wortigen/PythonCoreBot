class FileWorker:

    def __init__(self):
        self.path = ''
        self.File = None
        self.FileMode = ''
        self.base_path = ''
        self.config_path = ''
        self.temp_path = ''
        self.content = None
        self.type_content = None
        self.Errors = list()
        self.LoadConfig()

    def LoadConfig(self):
        global varObj
        config = varObj.get('config')
        self.config_path = config['config_path']
        self.temp_path = config['temp_path']
        self.base_path = config['app_path']

    def isExist(self, path = ''):
        if path == '':
            path = self.path
        return os.path.isfile(path)

    def CreateFileByContentByte(self, folder = '', name = 'test.txt', content = ''):
        if folder == '':
            folder = self.temp_path
        self.path = folder + '/' + name
        self.FileOpen('wb')
        self.File.write(content)
        self.FileClose()

    def CreateFile(self, folder = '', name = 'test.txt'):
        if folder == '':
            folder = self.temp_path
        self.path = folder + '/' + name
        self.FileOpen()
        self.FileClose()

    def FileWrite(self):
        self.FileOpen()
        if isinstance(self.content, list):
            for line in self.content:
                self.File.write(line + '\n')
        self.FileClose()

    def RefreshFile(self):
        if self.type_content == 'json':
            self.content = json.dumps(self.content)

        self.FileOpen()
        self.File.write(self.content)
        self.FileClose()

    def ReadFile(self):
        if self.isExist():
            self.FileOpen('r')
            self.content = self.File.readlines()
            self.type_content = 'None'
            self.FileClose()

    def ReadFileByte(self, path = ''):
        if path == '':
            path = self.path
        temp = open(path, 'rb')
        return temp

    def ContentByType(self, content_type = ''):
        if content_type != '':
            self.type_content = content_type

            if self.type_content == 'json':
                self.type_content = json.loads(self.content.replace("'", "\""))


    def Create(self):
        self.FileOpen()
        self.FileClose()

    def FileOpen(self, mode = 'w'):
        self.File = open(self.path, mode)

    def FileClose(self):
        self.File.close()

    # File folder path of app
    def FolderApp(self):
        return self.base_path

    def FolderTemp(self):
        return self.temp_path

    def FolderCongig(self):
        return self.config_path
