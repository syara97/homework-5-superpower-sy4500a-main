from VillainClass import *
class VillainChild(Villain):

    def __init__(self, name, hair, intelligence=0, strength=0, speed=0, durability=0, power=0, combat=0):
        self.hair = hair
        super().__init__(name, intelligence, strength, speed, durability, power, combat)

    def getStats(self):
        super().getStats()

    def getBonus(self):
        sumOfStats = super().getStats()
        if self.hair == 'None' or self.hair == "No Hair":
            sumOfStats += 20
        else:
            return False
        return sumOfStats