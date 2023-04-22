class Gobelin:
    def __init__(self, degat, loot):
        self.degat = degat
        self.loot = loot
    
    def randomDegat(self):
        self.degat = random.choice(range(3, 5))
        self.loot = random.choice(range(2, 2.4))