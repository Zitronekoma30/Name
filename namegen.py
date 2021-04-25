import random


with open("firstNames.txt", "r") as file:
    allFirstNames = file.read()
    firstNameList = allFirstNames.split("\n")

with open("lastNames.txt", "r") as file:
    allLastNames = file.read()
    lastNameList = allLastNames.split("\n")

def SetParams():
    amount = int(input("How many names would you like to generate? "))
    middleNames = int(input("How many middle names would you like? "))

    return amount, middleNames

def PrintNames(amount, middleNames):
    for i in range(amount):
        name = random.choice(firstNameList)
        if middleNames > 0:
            for i in range(middleNames):
                name += " " + random.choice(firstNameList)
        name += " " + random.choice(lastNameList)

        print(name)

a, m = SetParams()

PrintNames(a, m)
input("press any key to exit...")
