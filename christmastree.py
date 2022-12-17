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
    print("Season's Greetings")

def thingstosay(talk):
    print(talk)

def getname():
    name = input("what is your name?")

def hohohofunction():
    christmastree()
    seasongreeting()
    nameis = getname()
    print(nameis)
    # thingstosay(nameis)

hohohofunction()