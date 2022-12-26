import random
class Greeting:
    greetings = ["Season's Greetings", 
        "Happy Holidays", 
        "Felicioutous Festivities"]

    def seasongreeting():
        rand = random.randint(0,2)
        print(Greeting.greetings[rand])