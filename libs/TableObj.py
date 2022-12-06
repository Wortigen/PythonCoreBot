class TableObj:

    def __init__(self, name = ''):
        self.header = list()
        sefl.rows = list()
        self.type = None

    def GetHeader(self):
        return self.header

    def GetRows(self, ind = -1):
        if ind == -1:
            return self.rows
        else:
            if ind < len(self.rows):
                return self.rows[ind]
            else:
                return False
