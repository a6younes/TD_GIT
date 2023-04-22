from Team import Team


class PlayerTeam(Team):


    def init(self,members):
        super.init(members)
        self.nb_warriors
        self.nb_hunters 
        self.nb_wizards
        self.damage
        self.loot
        self.flee

    def getNbWarriors(self):
        return self.nb_warriors

    def getNbHunters(self):
        return self.nb_hunters

    def getNbWizards(self):
        return self.nb_wizards

    def getDamage(self):
        return self.damage

    def getLoot(self):
        return self.loot

    def getFlee(self):
        return self.flee