class DomainsObj:

    def __init__(self):
        self.id = -1
        self.domain = ''
        self.responsible = list()
        self.time_end = 0
        self.time_remember_easy = 0
        self.time_remember_hard = 0
        self.Hosting = ''
        self.IP = ''

    def GetStruct(self):
        return ['id','domain','responsible','time_end','time_remember_easy','time_remember_hard', 'Hosting', 'IP']

    def ToSave(self):
        temp = dict()
        temp['id'] = self.id
        temp['domain'] = self.domain
        temp['responsible'] = self.responsible
        temp['time_end'] = self.time_end
        temp['time_remember_easy'] = self.time_remember_easy
        temp['time_remember_hard'] = self.time_remember_hard
        temp['Hosting'] = self.Hosting
        temp['IP'] = self.IP
        return temp

    def ToLoad(self, attr = dict()):
        self.id = attr['id']
        self.domain = attr['domain']
        self.responsible = attr['responsible']
        self.time_end = attr['time_end']
        self.time_remember_easy = attr['time_remember_easy']
        self.time_remember_hard = attr['time_remember_hard']
        self.Hosting = attr['Hosting']
        self.IP = attr['IP']
