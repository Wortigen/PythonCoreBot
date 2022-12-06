class Core:

  def __init__(cls, param):
    cls.objects = dict()
    cls.action = list()
    cls.schema = list()
    cls.status = None
    cls.args = param

  def LoadAction(cls):
    pass

  def LoadObjects(cls):
    pass

  def SchemaLoad(cls):
     cls.schema = cls.args['schema']
     del cls.args['schema']
     temp = list()
     for x in cls.schema:
        if x.type == 'init':
            x.RunBuild()
        temp.append(x)
     cls.schema = temp
     del temp


  def Run(cls):
     global varObj
     varObj = Globals()
     varObj.save('config', cls.args)
     varObj.save('core', cls)

     cls.SchemaLoad()
     #cls.LoadObjects()
     #cls.LoadAction()

     print("App status: app run without errors")
