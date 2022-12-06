def StartUpApp():
    print("Start init action")

    global varObj
    core = varObj.get('core')
    config = varObj.get('config')

    #Preper start up files
    tempFile = FileWorker()

    tempFile.path = config["config_path"] + "/UserConfigs.txt"
    if tempFile.isExist() == False:
        tempFile.Create()
    else:
        tempFile.ReadFile()
        tempFile.type_content = 'json'
        tempFile.ContentByType()

        if isinstance(tempFile.content, list):
            tempFile.content = tempFile.content[0]
        if isinstance(tempFile.content, str):
            tempFile.content = json.loads(tempFile.content.replace("'", "\""))
        if isinstance(tempFile.content, dict):
            ind = tempFile.content.keys()
            users = dict()
            for x in ind:
                temp = UserObj()
                temp.ToLoad(tempFile.content[x])
                users[temp.id] = temp
            varObj.temp['tBot_user'] = users

            del users, ind
        tempFile.content = ''
        tempFile.type_content = None

    varObj.save('userFile', tempFile.path)

    tempFile.path = config["config_path"] + "/ChatConfigs.txt"
    if tempFile.isExist() == False:
        tempFile.Create()
    else:
        tempFile.ReadFile()
        tempFile.type_content = 'json'
        tempFile.ContentByType()

        if isinstance(tempFile.content, list):
            tempFile.content = tempFile.content[0]
        if isinstance(tempFile.content, str):
            tempFile.content = json.loads(tempFile.content.replace("'", "\""))
        if isinstance(tempFile.content, dict):
            ind = tempFile.content.keys()
            chats = dict()
            for x in ind:
                temp = ChatObj()
                temp.ToLoad(tempFile.content[x])
                chats[temp.id] = temp
            varObj.temp['tBot_chats'] = chats

            del chats, ind
        tempFile.content = ''
        tempFile.type_content = None

    varObj.save('chatFile', tempFile.path)

    tempFile.path = config["config_path"] + "/domains.csv"
    if tempFile.isExist() == False:
        tempFile.Create()
    else:
        pass

    varObj.save('domainsFile', tempFile.path)

    tempFile.path = config["config_path"] + "/domainsTemp.csv"
    varObj.save('domainsTempFile', tempFile.path)

    #telegram bot Structure
    tBotStructure = dict()

    #Add policy types
    tBotStructure['policy'] = list()
    tBotStructure['policy'] = ['guest', 'dev', 'SEO', 'HeadSEO', 'admin']
    tBotStructure['def_policy'] = ['quest']

    #Add list of commands
    tBotStructure['commands'] = ['start', 'help', 'back', 'finish', 'user',
    'user_edit', 'user_delete', 'user_list', 'user_list_guest', 'domains', 'list_domains', 'edit_domains',
    'chat', 'list_chat', 'edit_chat', 'delete_chat', 'files', 'empty_domains', 'get_domains', 'upload_domains',
    'text_comm']

    #Command structure
    tBotStructure['commands_structure'] = dict()
    tBotStructure['commands_structure']['user'] = list()
    tBotStructure['commands_structure']['user'] = ['user_edit', 'user_delete', 'user_list', 'user_list_guest', 'back']

    tBotStructure['commands_structure']['domains'] = list()
    tBotStructure['commands_structure']['domains'] = ['user_edit', 'user_delete', 'user_list', 'user_list_guest', 'back']

    tBotStructure['commands_structure']['chat'] = list()
    tBotStructure['commands_structure']['chat'] = ['list_chat', 'edit_chat', 'delete_chat', 'back']

    tBotStructure['commands_structure']['files'] = list()
    tBotStructure['commands_structure']['files'] = ['empty_domains', 'get_domains', 'upload_domains', 'back']

    #Policy structure
    tBotStructure['policy_structure'] = dict()
    tBotStructure['policy_structure']['guest'] = list()
    tBotStructure['policy_structure']['guest'] = ['start', 'help']

    tBotStructure['policy_structure']['SEO'] = list()
    tBotStructure['policy_structure']['SEO'] = ['start', 'help', 'back', 'finish', 'domains', 'list_domains', 'edit_domains',
    'chat', 'list_chat', 'edit_chat', 'delete_chat', 'files', 'empty_domains', 'get_domains', 'upload_domains',
    'text_comm']

    tBotStructure['policy_structure']['HeadSEO'] = list()
    tBotStructure['policy_structure']['HeadSEO'] = ['all']

    tBotStructure['policy_structure']['admin'] = list()
    tBotStructure['policy_structure']['admin'] = ['all']

    tBotStructure['policy_structure']['dev'] = list()
    tBotStructure['policy_structure']['dev'] = ['start', 'help', 'back', 'finish', 'files', 'empty_domains', 'get_domains', 'upload_domains']

    #Users default by username
    tBotStructure['wait_user'] = dict()
    tBotStructure['wait_user']['Wortigen'] = dict()
    tBotStructure['wait_user']['Wortigen'] = {'status': 'verefi', 'position': 'Admin', 'permission': ['admin']}

    tBotStructure['wait_user']['stefiienko'] = dict()
    tBotStructure['wait_user']['stefiienko'] = {'status': 'verefi', 'position': 'Dev', 'permission': ['dev']}

    tBotStructure['wait_user']['serhiiredko'] = dict()
    tBotStructure['wait_user']['serhiiredko'] = {'status': 'verefi', 'position': 'SEO', 'permission': ['SEO']}

    tBotStructure['wait_user']['klebanyaroslav'] = dict()
    tBotStructure['wait_user']['klebanyaroslav'] = {'status': 'verefi', 'position': 'SEO', 'permission': ['SEO']}

    tBotStructure['wait_user']['Redrive'] = dict()
    tBotStructure['wait_user']['Redrive'] = {'status': 'verefi', 'position': 'SEO', 'permission': ['HeadSEO']}

    varObj.save('tBot_config', tBotStructure)

    #Run base action threads
    core.objects['tBot'] = threading.Thread(target=StartBotAction)
    core.objects['tBot'].start()

    core.objects['main'] = threading.Thread(target=StartMainCoreAction)
    core.objects['main'].start()

    varObj.update('core', core)
