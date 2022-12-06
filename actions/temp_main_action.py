def StartMainCoreAction():
    global varObj
    domains = list()
    WorkThreading = True

    def ReadDocToDomains(path):
        File = FileWorker()
        File.path = path
        File.ReadFile()
        convert = Convertor()
        convert.set(File.content)
        print("File content from temp", File.content)

    while WorkThreading:
        if varObj.isExistKey('update_domain') == True:
            temp_domains = varObj.get('update_domain')
            ReadDocToDomains(temp_domains[list(temp_domains)[0]])
            del temp_domains[list(temp_domains)[0]]
            varObj.update('update_domain', temp_domains)
