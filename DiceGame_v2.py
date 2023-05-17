import random #this is called a module

# This prints/displays the welcome message
def printWelcomeMessage():
    print("Welcome to The Dice Game")

# This asks for input of how many players 
def askHowManyUsers(userNumberofPlayersAllowed): #userNumberofPlayers is an argument
    howManyUsers = int(input ("How many people are playing today (Maximum No is " +  str (userNumberofPlayersAllowed)+ ")?: "))
    return howManyUsers

def askUserName():
    userName = input ("what is your name?: ")
    return userName

def greetUser(userName):
    print("Hi", userName)

def getPlayerNamesList(totalNumberOfPlayers):
    playerNamesList = []  #this is the list that stores all player names
    for currentUserNumber in range(1, totalNumberOfPlayers + 1):
        print("Player", str(currentUserNumber)+", ", end="")
        currentPlayerName = askUserName()
        playerNamesList.append(currentPlayerName)
    return playerNamesList

def isThreePairs(aList):
    uniqueNumbersList = set(aList)
    isThreePairsBoolean = True

    for currentUniqueNumber in uniqueNumbersList:
        if aList.count(currentUniqueNumber) !=2:
            isThreePairsBoolean = False
    if isThreePairsBoolean == True:
        print ("-----------------------------------------------Great job! You got Three Pairs!")

    return isThreePairsBoolean   

def isTwoTriplets(aList):
    uniqueNumbersList = set(aList)
    isTwoTripletsBoolean = True

    if len(uniqueNumbersList) !=2:
        isTwoTripletsBoolean = False
    
    for currentUniqueNumber in uniqueNumbersList:
        if aList.count(currentUniqueNumber) !=3:
            isTwoTripletsBoolean = False
    if isTwoTripletsBoolean == True:
        print ("-----------------------------------------------Great job! You got Two Triplets!")
    return isTwoTripletsBoolean   

def isFourOfAKindAndPair(aList):
    uniqueNumbersDictionary = set(aList)  # This create dictionary {}
    uniqueNumbersList = list( uniqueNumbersDictionary ) # Convert the dictionary to a list []

    isFourOfAKindAndAPairBoolean = True
    
    if len( uniqueNumbersList ) != 2:
        isFourOfAKindAndAPairBoolean = False

    firstUniqueNumberCount = aList.count( uniqueNumbersList[0] )  
    # secondUniqueNumberCount = aList.count( uniqueNumbersList[1] )

    if firstUniqueNumberCount != 2 and firstUniqueNumberCount != 4:
        isFourOfAKindAndAPairBoolean = False

    if isFourOfAKindAndAPairBoolean == True:
        print( "----------------------------------------------Woohoo! You got a Four of a kind and a Pair!!!!" )
        
    return isFourOfAKindAndAPairBoolean


# the goal of this function is to use the list of names & player totals based on the input passed into from total number of players and returns both lists
def getPlayerResults(totalNumberOfPlayers, playerNamesList):

# this creates and returns both a player names list and their corresponding totals of their rolls based on the total number of players
    userDiceTotalsList = []
    userRollSubtotalList = []
    ONE_MULTIPLIER = 100
    FIVE_MULTIPLIER = 50
    THREE_OF_A_KIND_MULTIPLIER = 100
    FOUR_OF_A_KIND = 1000
    FIVE_OF_A_KIND = 2000
    SIX_OF_A_KIND = 3000
    STRAIGHT = 1500
    THREE_PAIRS = 1500
    TWO_TRIPLETS = 2500
    FOUR_OF_A_KIND_PLUS_A_PAIR = 1500
    HARD_STRAIGHT = 5000

    STRAIGHT_CONSTANT = 6

    currentNumberCount = 0
    for currentNameIndex in range(totalNumberOfPlayers):
        userInput = input(playerNamesList [currentNameIndex] + " Hit enter to Roll")
        currentUserDieValueList = rollDice()

        dieRangeEnd = len(currentUserDieValueList)
        
        for currentNumber in range(1, len(currentUserDieValueList)+1):
            if currentNumber in currentUserDieValueList:
                currentNumberCount = currentUserDieValueList.count(currentNumber)
            else:
                currentNumberCount = 0

            if currentNumber == 1:
                if currentNumberCount < 4:
                    userRollSubtotalList.append(currentNumberCount*ONE_MULTIPLIER)
            if currentNumber == 5:
                if currentNumberCount < 3:
                    userRollSubtotalList.append(currentNumberCount*FIVE_MULTIPLIER)

            if currentNumber == 2:
                if currentNumberCount == 3:
                    userRollSubtotalList.append(currentNumber*THREE_OF_A_KIND_MULTIPLIER)
            if currentNumber == 3:
                if currentNumberCount == 3:
                    userRollSubtotalList.append(currentNumber*THREE_OF_A_KIND_MULTIPLIER)
            if currentNumber == 4:
                if currentNumberCount == 3:
                    userRollSubtotalList.append(currentNumber*THREE_OF_A_KIND_MULTIPLIER)
            if currentNumber == 5:
                if currentNumberCount == 3:
                    userRollSubtotalList.append(currentNumber*THREE_OF_A_KIND_MULTIPLIER)
            if currentNumber == 6:
                if currentNumberCount == 3:
                    userRollSubtotalList.append(currentNumber*THREE_OF_A_KIND_MULTIPLIER)

        # Below is for 4 of a kind through 6 of a kind
            if currentNumberCount == 4:
                userRollSubtotalList.append(FOUR_OF_A_KIND)
            if currentNumberCount == 5:
                userRollSubtotalList.append(FIVE_OF_A_KIND)
            if currentNumberCount == 6:
                userRollSubtotalList.append(SIX_OF_A_KIND)

         # Below is for a straight
            if len(set(currentUserDieValueList)) == STRAIGHT_CONSTANT:
                userRollSubtotalList = []
                userRollSubtotalList.append(STRAIGHT)
                break
       
         # Below is for a Three Pairs
            if isThreePairs(currentUserDieValueList):
                userRollSubtotalList = []
                userRollSubtotalList.append(THREE_PAIRS)
                break

         # Below is for a Two Triplets
            if isTwoTriplets(currentUserDieValueList):
                userRollSubtotalList = []
                userRollSubtotalList.append(TWO_TRIPLETS)
                break

         # Below is for Four of Kind and a Pair
            if isFourOfAKindAndPair(currentUserDieValueList):
                userRollSubtotalList = []
                userRollSubtotalList.append(FOUR_OF_A_KIND_PLUS_A_PAIR)
                break


        currentUserDieTotal = getScoreofRollDice(userRollSubtotalList)
        userDiceTotalsList.append(currentUserDieTotal)
        # print("Great Job! Your roll is:", currentUserDieValueList, "\nYour total is:", currentUserDieTotal)
        print("Great Job! Your roll is:", currentUserDieValueList, "your total is:", sum(userRollSubtotalList),end="\n \n")
        currentNumberCount = 0
        userRollSubtotalList = []

    return userDiceTotalsList

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


def getScoreofRollDice(aListofSubtotals):
    return sum(aListofSubtotals)

    # below is the same as the one line above
    # totalOfRoll = sum(aListofSubtotals)
    # return totalOfRoll


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
    userKeepPlaying = "y"

    NUMBER_OF_PLAYERS_ALLOWED = 6
    printWelcomeMessage() #don't forget parenthesis to call the function
    howManyUsersInMain = askHowManyUsers(NUMBER_OF_PLAYERS_ALLOWED)

    while howManyUsersInMain > NUMBER_OF_PLAYERS_ALLOWED:
        revisedNumberofUsers = int(input ("Sorry, the maximum number of players is: " + str (NUMBER_OF_PLAYERS_ALLOWED) + ", please enter again: "))
        howManyUsersInMain = revisedNumberofUsers

    playerNamesList = getPlayerNamesList(howManyUsersInMain)

    while userKeepPlaying == "y":
        playersTotalsListinMain = getPlayerResults(howManyUsersInMain, playerNamesList)
        determineWinner(playerNamesList, playersTotalsListinMain)
        userKeepPlaying = input ("Do you want to play again? Type y for YES or n for NO: ")


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

# This is the old function that adds face value of the dice.
# def getSumOfRollDice(userDieValueList): #userDieValueList is a parameter (placeholder)
#     sumOfRollDice = 0
#     for currentDieValue in userDieValueList:
#         sumOfRollDice = sumOfRollDice + currentDieValue 
#     return sumOfRollDice

# This function checks for how many occurences of a die value.
# def singleNumberExists(anyList, phDieValue):
#     if phDieValue in anyList:
#         return True
#     else:
#         return False

# four of a kind and a pair
# Two triplets
# Hard straight (1,2,3,4,5,6)
# Cute messages
# Tie issue
# Leaderboard
# One Roll or Full game



