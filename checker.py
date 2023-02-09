import random
from gift import Gift
class Checker:
    def __init__(self, behave, presents):
        self.behave = behave
        # self.presents =["doll", "car", "ball", "orange"]

    def ask_question(self):
        self.behave = input("Have you been Naughty or Nice?")
        return self.check_naughty_nice(self, self.behave)

    def check_naughty_nice(self, behave):
        if behave.lower() =="nice":
            return self.gift(True)
        elif behave.lower() == "naughty":
            return self.gift(False)
        else:
            print("Error with answer. Use Naughty or Nice only.")
            return self.ask_question(self)

    def gift(bool, self):
        if bool==False:
            return "lump of coal"
        else:
            end = len(self.present)-1
            rand = random.randint(0,end)
            return "Your gift this year is: " + self.present[rand]