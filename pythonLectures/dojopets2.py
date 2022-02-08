
class ninja:
    def __init__(self, firstname, lastname, treats, pet_food,):
        self.firstname = firstname
        self.lastname = lastname
        self.treats = treats
        self.pet_food = pet_food


class pet:
    def __init__(self, type, tricks, noise, name):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 75
        self.noise = noise 

    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health  += 10
    def play(self):
        self.health += 5
        self.energy -= 15
        return self
    def noise(self):
        print(self.noise)
        return self
