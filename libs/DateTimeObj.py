class DateTimeObj:
    def __init__(self):
        self.DateTime = 0
        self.Time = 0
        self.Date = 0
        self.strDate = ''
        self.strTime = ''
        self.CurrentDateTime()
        self.StringDate()
        self.StringTime()
        self.CurrentTime()
        self.CurrentDate()

    def CurrentDateTime(self):
        self.DateTime = int(time.time())

    def CurrentTime(self):
        res = time.localtime(self.DateTime)
        self.Time = res.tm_sec
        self.Time += 60 * res.tm_min
        self.Time += 60 * 60 * res.tm_hour

    def CurrentDate(self):
        self.Date = self.DateTime - self.Time

    def StringDate(self):
        res = time.localtime(self.DateTime)
        self.strDate = res.tm_mday + "." + res.tm_mon + ":" + res.tm_year

    def StringTime(self):
        res = time.localtime(self.DateTime)
        self.strDate = res.tm_hour + ":" + res.tm_min + ":" + res.tm_sec

    def Update(self):
        self.CurrentDateTime()
        self.StringDate()
        self.StringTime()
        self.CurrentTime()
        self.CurrentDate()
