import random
class Gift:
    presents =["doll", "car", "ball", "orange", "board game", "paints"]

    def gift(bool):
            if bool==False:
                print("Your gift this year is: a lump of coal")
            else:
                end = len(Gift.presents)-1
                rand = random.randint(0,end)
                print("Your gift this year is: " + Gift.presents[rand])