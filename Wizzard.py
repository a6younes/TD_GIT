import random

class Wizard:
    def __init__(self):
        self.damage = random.randint(2, 4)
        self.chance = 20
        self.escape = 10
        self.price = 15
        self.unit_type = "wizard"