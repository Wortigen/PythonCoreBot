class Globals(object):

    @classmethod
    def __init__(self):
        self.list = dict()
        self.temp = dict()

    @classmethod
    def save(cls, name, value):
        if name not in cls.list.keys():
            cls.list[name] = value
        else:
            cls.list[name+"_copy_1"] = valae
        return True

    def isExistKey(self, key):
        if key in self.list.keys():
            return True
        else:
            return False

    @classmethod
    def update(cls, name, value):
        if name in cls.list.keys():
            cls.list[name] = value
        else:
            return False
        return True

    @classmethod
    def get(cls, name):
        if name in cls.list.keys():
            return cls.list[name]
        else:
            return None

    @classmethod
    def delete(cls, name):
        del cls.list[name]
        return True
