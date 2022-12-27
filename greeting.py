import random
from user import User

class Greeting:
    greetings = ["Season's Greetings", 
        "Happy Holidays", 
        "Felicioutous Festivities"]

    def seasongreeting():
        rand = random.randint(0,2)
        username = User.name
        print(Greeting.greetings[rand] + username +"!")