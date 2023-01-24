class Checker:
    def __init__(self, state):
        self.state = state

    def ask_question(self):
        self.state = input("Have you been Naughty or Nice?")
        return self.state

    def check_naughty_nice(self):
        if self.state.lower() =="nice":
            return True
        elif self.state.lower() == "naughty":
            return False
        else:
            print("Error with answer. Use Naughty or Nice only.")
            return self.ask_question()