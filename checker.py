import random
class Checker:
    def __init__(self, behave, presents):
        self.behave = behave
        self.presents =["doll", "car", "ball", "orange"]

    def ask_question(self):
        self.behave = input("Have you been Naughty or Nice?")
        return self.check_naughty_nice(self, self.behave)

    def check_naughty_nice(self, behave):
        if behave.lower() =="nice":
            return True
        elif behave.lower() == "naughty":
            return False
        else:
            print("Error with answer. Use Naughty or Nice only.")
            return self.ask_question(self)

    def gift(bool, self):
        if bool==False:
            return "lump of coal"
        else:
            rand = random.randint(0,3)
            return self.present[rand]