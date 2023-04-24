from HeroClass import *
class HeroChild(Hero):

    def __init__(self, name, race, intelligence=0, strength=0, speed=0, durability=0, power=0, combat=0):
        self.race = race
        super().__init__(name, intelligence, strength, speed, durability, power, combat)

    def getStats(self):
        super().getStats()

    def getBonus(self):
        sumOfStats = super().getStats()
        if self.race == 'Human':
            sumOfStats -= 7
        elif self.race == 'God/Eternal':
            sumOfStats += 20
        else:
            return False
        return sumOfStats