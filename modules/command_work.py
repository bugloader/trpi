class CommandWork:
    def __init__(self, argv):
        self.argv = argv

    def help(self):
        f = open("data/command_help.txt", "r")
        print(f.read())
        f.close()
        return True

    def install(self):
        pass

    def remove(self):
        pass

    def search(self):
        pass

    def list(self):
        pass

    def show(self):
        pass

    def addserver(self):
        pass

    def removeserver(self):
        pass

    def regserver(self):
        pass

    def loginaccount(self):
        pass

    def gui(self):
        pass
