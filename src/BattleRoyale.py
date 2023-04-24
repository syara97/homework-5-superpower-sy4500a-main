import csv
from HeroClass import *
from VillainClass import *

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



    print("Heroes: ", end="")
    for hero in heroesNVillainsList:
        print(hero.name, end=", ")
    print()

    print("Villains: ", end="")
    for villain in heroesNVillainsList:
        print(villain.name, end=", ")
    print()