class Villain(object):

    def __init__(self, name, intelligence=0, strength=0, speed=0, durability=0, power=0, combat=0):
        self.__name = name
        self.__intelligence = int(intelligence)
        self.__strength = int(strength)
        self.__speed = int(speed)
        self.__durability = int(durability)
        self.__power = int(power)
        self.__combat = int(combat)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def intelligence(self):
        return self.__intelligence

    @intelligence.setter
    def intelligence(self, newIntelligence):
        assert isinstance(newIntelligence, int), "Attribute should be an integer"
        assert newIntelligence in range(0, 106), "The integer should be between 0 and 105"
        self.__intelligence = newIntelligence

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, newStrength):
        assert isinstance(newStrength, int), "Attribute should be an integer"
        assert newStrength in range(0, 106), "The integer should be between 0 and 105"
        self.__strength = newStrength

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, newSpeed):
        assert isinstance(newSpeed, int), "Attribute should be an integer"
        assert newSpeed in range(0, 106), "The integer should be between 0 and 105"
        self.__speed = newSpeed

    @property
    def durability(self):
        return self.__durability

    @durability.setter
    def durability(self, newDurability):
        assert isinstance(newDurability, int), "Attribute should be an integer"
        assert newDurability in range(0, 106), "The integer should be between 0 and 105"
        self.__durability = newDurability

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, newPower):
        assert isinstance(newPower, int), "Attribute should be an integer"
        assert newPower in range(0, 106), "The integer should be between 0 and 105"
        self.__power == newPower

    @property
    def combat(self):
        return self.__combat

    @combat.setter
    def combat(self, newCombat):
        assert isinstance(newCombat, int), "Attribute should be an integer"
        assert newCombat in range(0, 106), "The integer should be between 0 and 105"
        self.__combat = newCombat

    def getStats(self):
        sumOfStats = self.strength + self.speed + self.durability
        return sumOfStats

    def getBonus(self):
        sumOfStats = self.getStats()
        if self.strength >= 85:
            sumOfStats += 10
        elif self.durability <= 50:
            sumOfStats -= 10
        else:
            return False
        return sumOfStats

