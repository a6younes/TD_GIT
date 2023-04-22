class Zombie:
    def __init__(self, degat, loot):
        self.degat = degat
        self.loot = loot
    
    def randomDegat(self):
        self.degat = random.choice(range(1, 2))
        self.loot = random.choice(range(0.5, 1))