import random
from user import User

class Greeting:
    greetings = ["Season's Greetings", 
        "Happy Holidays", 
        "Felicioutous Festivities",
        "Comfort and Joy",
        "Warmest Wishes",
        "Happy Yultide",
        "Be Merry",
        "Glad Tidings"]

    def seasongreeting():
        rand = random.randint(0,2)
        username = User.name
        print(Greeting.greetings[rand] + " " + username +"!")