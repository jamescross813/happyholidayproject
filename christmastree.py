import random
class ChristmasTree:
    def christmastree():
        print("      ^      ")
        print("     / \     ")
        print("    /___\    ")
        print("   /     \   ")
        print("  /_______\  ")
        print("  /       \  ")
        print(" /_________\ ")
        print("     | |     ")
        print("    |___|    ")

    def seasongreeting():
        greetings = ["Season's Greetings", "Happy Holidays", "Felicioutous Festivities"]
        rand = random.randint(0,2)
        print(greetings[rand])

    def thingstosay(talk):
        print(talk)

    def getname():
        name = input("what is your name?")
        return name

    def hohohofunction():
        christmastree()
        seasongreeting()
        nameis = getname()
        # print(nameis)
        thingstosay("hello " + nameis)

    hohohofunction()