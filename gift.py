import random
class Gift:
    presents =["doll", "car", "ball", "orange", "board game", "paints"]

    def gift(bool):
            if bool==False:
                return "lump of coal"
            else:
                end = len(Gift.presents)-1
                rand = random.randint(0,end)
                return "Your gift this year is: " + self.present[rand]