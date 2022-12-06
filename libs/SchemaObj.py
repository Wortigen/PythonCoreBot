class SchemaDate(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.struct = dict()

    def ConfigStruct(cls, struct):
        cls.struct = struct

    def RunBuild(cls):
        print(f"Start work schema: {cls.name}")
        active = ActivatorAction()
        for act in cls.struct['actions']:
            active.add(act)
        if 'objects' in cls.struct.keys():
            listObj = cls.struct['objects']
            active.SetObj(listObj)

        active.Run()

    def ShowName(cls):
        return cls.name

    def ShowType(cls):
        return cls.type

    def GetObjects(cls):
        return cls.struct['objects']

    def GetActions(cls):
        return cls.struct['actions']

    def GetObjReview(cls):
        pass
