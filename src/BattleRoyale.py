import csv
from HeroClass import *
from VillainClass import *
from HeroChild import *
from VillainChild import *

with open('../SuperpowerDataset.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    powerList = []
    heroesNVillainsList = []

    #for row in reader:
     #   print(row['Alignment'], row['Name'])

    for row in reader:
        if row['Alignment'] == 'good':
            heroObject = Hero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            heroesNVillainsList.append(heroObject)
        elif row['Alignment'] == 'bad' or row['Alignment'] == 'neutral':
            villainObject = Villain(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            heroesNVillainsList.append(villainObject)
        elif row['Alignment'] == 'good' and (row['Race'] == 'Human' or row['Race'] == 'God/Eternal'):
            childHeroObject = HeroChild(row['Name'], row['Race'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            heroesNVillainsList.append(childHeroObject)
        elif row['Alignment'] == 'bad' and (row['Hair'] == 'None' or row['Hair'] == 'No Hair'):
            childVillainObject = VillainChild(row['Name'], row['Hair'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            heroesNVillainsList.append(childVillainObject)

    winCount = {}
    loseCount ={}
    tieCount ={}

    def fightCount(object, result):
        if result == "Wins":
            if object in winCount:
                winCount[object] += 1
            else:
                winCount[object] = 1
        elif result == "Loses":
            if object in loseCount:
                loseCount[object] += 1
            else:
                loseCount[object] = 1
        elif result == 'Ties':
            if object in tieCount:
                tieCount[object] += 0.5
            else:
                tieCount[object] = 0.5

    for object in range(len(heroesNVillainsList)):
        for character in range(object + 1, len(heroesNVillainsList)):
            object1 = heroesNVillainsList[object]
            object2 = heroesNVillainsList[character]
            if object1 != object2:
                object1Score = object1.getBonus()
                object2Score = object2.getBonus()
                if object1Score > object2Score:
                    fightCount(object1.name, "Wins")
                    fightCount(object2.name, "Loses")
                elif object2Score > object1Score:
                    fightCount(object2.name, "Wins")
                    fightCount(object2.name, "Loses")
                else:
                    fightCount(object1.name, "Ties")
                    fightCount(object2.name, "Loses")

    totalScores = {}
    for object in heroesNVillainsList:
        wins = winCount.get(object.name, 0)
        ties = tieCount.get(object.name, 0)
        losses = loseCount.get(object.name, 0)
        totalScores[object] = wins + ties - losses

    bestObject = max(totalScores, key=totalScores.get)
    worstObject = min(totalScores, key=totalScores.get)
    print("THE BEST AND WORST BATTLE ROYAL FIGHTERS ARE: ")
    print(f"The character with the best record is: {bestObject.name} a {type(bestObject).__name__}, with a total score of {totalScores[bestObject]}.")
    print(f"The character with the worst record is: {worstObject.name} a {type(worstObject).__name__}, with a total score of {totalScores[worstObject]}.")
    print()
    print("THESE ARE ALL THE HEROES AND VILLAINS INDIVIDUAL STATS: ")
    print()
    for object in heroesNVillainsList:
        wins = winCount.get(object.name, 0)
        ties = tieCount.get(object.name, 0)
        losses = loseCount.get(object.name, 0)
        print(f"{object.name}, a {type(object).__name__} has: {wins} wins, {losses} losses, {ties} ties.")


