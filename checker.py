class Checker:
    def __init__(self, state):
        self.state = state

    def ask_question(self):
        self.state = input("Have you been Naughty or Nice?")
        return self.state

    def check_naughty_nice(self):
        if self.state.lower() =="nice":
            return True
        return False