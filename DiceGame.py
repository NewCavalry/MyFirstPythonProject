import random #this is called a module

# This prints/displays the welcome message
def printWelcomeMessage():
    print("Welcome to The Dice Game")

# This asks for input of how many players 
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

# this creates and returns both a player names list and their corresponding totals of their rolls based on the total number of players
    userDiceTotalsList = []
    for currentNameIndex in range(totalNumberOfPlayers):
        userInput = input(playerNamesList [currentNameIndex] + " Hit enter to Roll")
        currentUserDieValueList = rollDice()
        currentUserDieTotal = getSumOfRollDice(currentUserDieValueList)
        userDiceTotalsList.append(currentUserDieTotal)
        # print("Great Job! Your roll is:", currentUserDieValueList, "\nYour total is:", currentUserDieTotal)
        print("Great Job! Your roll is:", currentUserDieValueList)
    return playerNamesList, userDiceTotalsList

# This function uses the random module to create a list of random numbers between 1 and 6
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

# This determines the winner and writes to a file with list of winner names
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

    # List of Winners
    # This opens the file in append mode which adds to the file
    winningListFile = open("winningList.txt", "a")

    # This is to write to the file
    winningListFile.write("Winner: " + winnerName + "  Winning Number: " + str(winningNumber)+ "\n")

    # Always have to close the file to stop buffer from overflowing (save resources in memory)
    winningListFile.close()

    # Can add a track function

def readListofWinners():
    winningListFile = open("winningList.txt", "r")
    line = winningListFile.readline().rstrip("\n")
    while line != "":
        print(line)
        line = winningListFile.readline().rstrip("\n")
    winningListFile.close()

def main():
    numberOfPlayersAllowed = 6
    printWelcomeMessage() #don't forget parenthesis to call the function
    howManyUsersInMain = askHowManyUsers(numberOfPlayersAllowed)

    while howManyUsersInMain > numberOfPlayersAllowed:
        revisedNumberofUsers = int(input ("Sorry, the maximum number of players is: " + str (numberOfPlayersAllowed) + ", please enter again: "))
        howManyUsersInMain = revisedNumberofUsers
        
    playerNamesListinMain, playersTotalsListinMain = getPlayerResults(howManyUsersInMain)
    determineWinner(playerNamesListinMain, playersTotalsListinMain)
    playerResponse = input ("Do you want to see winner results? Type y or n ")
    print()
    if playerResponse == "y": 
        readListofWinners()
    print("\nGood game!")

main() #calls the function

# ---------------------  
# def push(): 
#     return baby
# doctorsHands = push()


