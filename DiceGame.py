import random

def rollDice():
    numberOfDice = 6
    dieRangeStart = 1
    dieRangeEnd = 6

    dieValuesList = [] #to store the roll values for each die
    for currentDie in range(numberOfDice):
        randomNumber = random.randint(dieRangeStart, dieRangeEnd)
        dieValuesList.append(randomNumber) #appends (or adds) randomNumber to the dieValuesList
    return dieValuesList

def getSumOfRollDice(userDieValueList):
    sumOfRollDice = 0
    for currentDieValue in userDieValueList:
        sumOfRollDice = sumOfRollDice + currentDieValue 
    return sumOfRollDice

def main():
    dieValuesListInMain = rollDice()
    print(dieValuesListInMain)
    sumOfRollDiceInMain = getSumOfRollDice(dieValuesListInMain)
    print("Great job! This is your current total!", sumOfRollDiceInMain)


main()

