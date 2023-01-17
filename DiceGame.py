import random #this is called a module

def printWelcomeMessage():
    print("Welcome to The Dice Game")

def askHowManyUsers(userNumberofPlayersAllowed): #userNumberofPlayers is an argument
    howManyUsers = int(input ("How many people are playing today? Maximum No: " +  str (userNumberofPlayersAllowed)+ " "))
    return howManyUsers

def askUserName():
    userName = input ("what is your name?: ")
    return userName

def greetUser(userName):
    print("Hi", userName)

# the goal of this function is to populate a list of: player names & player totals based on the input passed into from total number of players and returns both lists
def getPlayerResults(totalNumberOfPlayers):
    playerNamesList = []  #this is the list that stores all player names
    for currentUserNumber in range(1, totalNumberOfPlayers + 1):
        print("Player", str(currentUserNumber)+", ", end="")
        currentPlayerName = askUserName()
        playerNamesList.append(currentPlayerName)

    userDiceTotalsList = []
    for currentNameIndex in range(totalNumberOfPlayers):
        userInput = input(playerNamesList [currentNameIndex] + " Hit enter to Roll")
        currentUserDieValueList = rollDice()
        currentUserDieTotal = getSumOfRollDice(currentUserDieValueList)
        userDiceTotalsList.append(currentUserDieTotal)
        # print("Great Job! Your roll is:", currentUserDieValueList, "\nYour total is:", currentUserDieTotal)
        # print("Great Job! Your roll is:", currentUserDieValueList)
    return playerNamesList, userDiceTotalsList

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
def determineWinner(playerNames, playerTotals):
    # numberOfPlayers = len(playerNames)

    # get highest totals from player total list
    winningNumber = max(playerTotals)

    # find index of highest score from player total list
    winningNumberIndex = playerTotals.index(winningNumber)

    # use index to display the corresponding name from names list
    winnerName = playerNames [winningNumberIndex]

    # print out the name along with the total for the winner
    print("Congratulations!", winnerName, "you won with a total of:", winningNumber)


def main():
    numberOfPlayersAllowed = 6
    printWelcomeMessage() #don't forget parenthesis to call the function
    howManyUsersInMain = askHowManyUsers(numberOfPlayersAllowed)

    while howManyUsersInMain > numberOfPlayersAllowed:
        revisedNumberofUsers = int(input ("sorry, the maximum number of players is " + str (numberOfPlayersAllowed) + ", please enter again: "))
        howManyUsersInMain = revisedNumberofUsers
        
    playerNamesListinMain, playersTotalsListinMain = getPlayerResults(howManyUsersInMain)
    determineWinner(playerNamesListinMain, playersTotalsListinMain)

main() #calls the function

# ---------------------  
# def push(): 
#     return baby
# doctorsHands = push()


