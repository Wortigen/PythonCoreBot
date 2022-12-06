class Convertor(object):

    def __init__(self):
        self.Data = None

    def Set(self, data):
        self.Data = data

    def Get(self):
        return self.Data

    def CSVHeaderConvert(self):
        self.Data = ",".join(self.Data)

    def FromFileToCSVTable(self):
        print(self.Data)
