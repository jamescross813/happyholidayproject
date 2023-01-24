class Checker:
    

    def ask_question(self):
        self.state = input("Have you been Naughty or Nice?")
        return self.state

    def check_naughty_nice(ans):
        if ans=="yes":
            return True
        return False