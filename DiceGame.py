import random #this is called a module

def printWelcomeMessage():
    print("Welcome to The Dice Game")

def askHowManyUsers(userNumberofPlayersAllowed): #userNumberofPlayers is an argument
    howManyUsers = int(input ("How many people are playing today? Maximum No: " +  str (userNumberofPlayersAllowed)+ " "))
    return howManyUsers

def askUserName():
    userName = input ("What is your name?: ")
    return userName

def greetUser(userName):
    print("Hi", userName)

def getPlayerResults(totalNumberOfPlayers):
    playerNamesList = []
    for currentUserNumber in range(1, totalNumberOfPlayers + 1):
        print("Player", currentUserNumber,)
        currentPlayerName = askUserName()
        playerNamesList.append(currentPlayerName)

    for currentNameIndex in range(totalNumberOfPlayers):
        userInput = input(playerNamesList [currentNameIndex] + " Hit enter to Roll")
        currentUserDieValueList = rollDice()
        currentUserDieTotal = getSumOfRollDice(currentUserDieValueList)
        print(currentUserDieValueList)

    return playerNamesList


def rollDice(): #defining a function
    numberOfDice = 6
    dieRangeStart = 1 #relates to the randint function
    dieRangeEnd = 6 #relates to the randint function
    dieValuesList = [] #to store the roll values for each die
    for currentDie in range(numberOfDice): #determines how many times the loop runs
        randomNumber = random.randint(dieRangeStart, dieRangeEnd)
        dieValuesList.append(randomNumber) #appends (or adds) randomNumber to the dieValuesList
    return dieValuesList

# This function take in a user list accumulates it and then returns it.
def getSumOfRollDice(userDieValueList): #userDieValueList is a parameter (placeholder)
    sumOfRollDice = 0
    for currentDieValue in userDieValueList:
        sumOfRollDice = sumOfRollDice + currentDieValue 
    return sumOfRollDice
# 
def main():
    numberOfPlayersAllowed = 6
    printWelcomeMessage() #don't forget parenthesis to call the function
    howManyUsersInMain = askHowManyUsers(numberOfPlayersAllowed)

    while howManyUsersInMain > numberOfPlayersAllowed:
        revisedNumberofUsers = int(input ("sorry, the maximum number of players is " + str (numberOfPlayersAllowed) + ", please enter again: "))
        howManyUsersInMain = revisedNumberofUsers
        
    playerNamesListinMain = getPlayerResults(howManyUsersInMain)
    print (playerNamesListinMain)

main() #calls the function

# ---------------------  
# def push(): 
#     return baby
# doctorsHands = push()


