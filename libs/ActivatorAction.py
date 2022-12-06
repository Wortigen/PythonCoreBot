class ActivatorAction(object):

    def __init__(self):
        self.actions = list()
        self.obj = dict()
        self.save = dict()
        self.temp = dict()
        self.work = dict()

    def add(cls, action):
        cls.actions.append(action)

    def SetObj(cls, objs):
        print("Object is upload")
        #if type(objs) == 'dict':
            #pass

    def Run(cls):
        print("List actions in Activator =>",cls.actions)
        for act in cls.actions:
            cls.command(act)
            cls.Do()


    def command(cls, act):
        if "obj" in act.keys():
            cls.getObj(act['obj'])
        if "do" in act.keys():
            cls.getAction(act['do'])
        if "act" in act.keys():
            cls.getActionToDo(act['act'])
        cls.attribute(act)

    def Do(cls):
        if 'type' in cls.work.keys() and cls.work['type'] == 'run_script':
            #print(f"Action will start :=> {cls.work['type']} -> {cls.work['func']}")
            if 'func_args' in cls.work.keys():
                exec(cls.work['func']+'(cls.work["func_args"])')
            else:
                exec(cls.work['func'] + '()')
        cls.work = dict()

    def getObj(cls, obj):
        pass

    def getAction(cls, act):
        if act == "read":
            pass
        if act == "save":
            pass
        if act == "act":
            cls.work['type'] = 'run_script'

    def getActionToDo(cls, todo):
        if cls.work['type'] == "run_script":
            cls.work['func'] = todo
        else:
            pass

    def attribute(cls, attr):
        for key in attr.keys():
            if key == "name":
                pass
            if key == "target":
                pass
            if key == "keyData":
                cls.work['func_args'] = attr[key]
