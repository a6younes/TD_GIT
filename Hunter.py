import random

class Hunter:
    def __init__(self):
        self.damage = random.randint(1, 2)
        self.chance = 10
        self.escape = 20
        self.price = 25
        self.unit_type = "hunter"