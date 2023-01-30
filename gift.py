import random
class Gift:
    def __init__(self, presents):
        self.presents =["doll", "car", "ball", "orange"]

    def gift(bool, self):
            if bool==False:
                return "lump of coal"
            else:
                end = len(self.present)-1
                rand = random.randint(0,end)
                return "Your gift this year is: " + self.present[rand]