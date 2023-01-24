class Checker:
    def __init__(self, behave):
        self.behave = behave

    def ask_question(self):
        self.behave = input("Have you been Naughty or Nice?")
        return self.check_naughty_nice(self, self.behave)

    def check_naughty_nice(self, behave):
        if behave.lower() =="nice":
            print("good job!")
            return True
        elif behave.lower() == "naughty":
            print("uh oh")
            return False
        else:
            print("Error with answer. Use Naughty or Nice only.")
            return self.ask_question()