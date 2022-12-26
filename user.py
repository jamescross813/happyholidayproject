class User:
    def __init__(self, name):
        self.name = name

    def getname(self):
        self.name = input("what is your name?")
        return self.name