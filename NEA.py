#Import Libraries
import random

#Player Card Arrays
p1Cards = []
p2Cards = []

#User Details/Logins
usernames = ["eboaden","admin","guest","dferreira"]
userDetails = [["Edward","Boaden","Passw0rd"],["Admin","User","Passw0rd"],["Guest","User","Passw0rd"],["Daniel","Ferreira","Passw0rd"]]

#Player 1 Login
print("Player 1:")
while True:
    username = input("Username: ")
    if username in usernames:
        userIndex = usernames.index(username)
        password = input("Password: ")
        if password == userDetails[userIndex][2]:
            p1fname = userDetails[userIndex][0]
            p1lname = userDetails[userIndex][1]
            p1username = username
            print("Welcome",p1fname,p1lname)
            break
        else:
            print("Incorrect Password")
    else:
        print("Incorrect Username")

#Player 2 Login
print("Player 2:")
while True:
    username = input("Username: ")
    if username in usernames:
        if username != p1username:
            userIndex = usernames.index(username)
            password = input("Password: ")
            if password == userDetails[userIndex][2]:
                p2fname = userDetails[userIndex][0]
                p2lname = userDetails[userIndex][1]
                print("Welcome",p2fname,p2lname)
                break
            else:
                print("Incorrect Password")
        else:
            print(p1username,"is already logged in")
    else:
        print("Incorrect Username")

#Check cards function to calculate the winning player 
def checkCards(p1Card,p2Card):
    p1Color = p1Card[0]
    p1Number = p1Card[1]
    p2Color = p2Card[0]
    p2Number = p2Card[1]
    if p1Color == p2Color:
        if p2Number < p1Number:
            print("Player 1 Wins")
            p1Cards.append(p1Card)
            p1Cards.append(p2Card)
        else:
            print("Player 2 Wins")
            p2Cards.append(p1Card)
            p2Cards.append(p2Card)
    else:
        if p1Color == "Red" and p2Color == "Black":
            print("Player 1 Wins")
            p1Cards.append(p1Card)
            p1Cards.append(p2Card)
        elif p1Color == "Black" and p2Color == "Red":
            print("Player 2 Wins")
            p2Cards.append(p1Card)
            p2Cards.append(p2Card)
        elif p1Color == "Yellow" and p2Color == "Red":
            print("Player 1 Wins")
            p1Cards.append(p1Card)
            p1Cards.append(p2Card)
        elif p1Color == "Red" and p2Color == "Yellow":
            print("Player 2 Wins")
            p2Cards.append(p1Card)
            p2Cards.append(p2Card)
        elif p1Color == "Black" and p2Color == "Yellow":
            print("Player 1 Wins")
            p1Cards.append(p1Card)
            p1Cards.append(p2Card)
        elif p1Color == "Yellow" and p2Color == "Black":
            print("Player 2 Wins")
            p2Cards.append(p1Card)
            p2Cards.append(p2Card)
        else:
            print("Error")
    print(" ")

#Deck of Cards
deck = [["Red",1],["Red",2],["Red",3],["Red",4],["Red",5],["Red",6],["Red",7],["Red",8],["Red",9],["Red",10],
        ["Yellow",1],["Yellow",2],["Yellow",3],["Yellow",4],["Yellow",5],["Yellow",6],["Yellow",7],["Yellow",8],["Yellow",9],["Yellow",10],
        ["Black",1],["Black",2],["Black",3],["Black",4],["Black",5],["Black",6],["Black",7],["Black",8],["Black",9],["Black",10]]

#Run Main Program until deck is empty
while len(deck) != 0:
    random.shuffle(deck)
    input("Player 1 Pick Card ")
    p1Card = deck[0]
    print("Your Card is",p1Card[0],str(p1Card[1]))
    input("Player 2 Pick Card ")
    p2Card = deck[1]
    print("Your Card is",p2Card[0],str(p2Card[1]))
    checkCards(p1Card,p2Card)
    deck.remove(p1Card)
    deck.remove(p2Card)

#Print player scores
print("Scores:")
if len(p1Cards) > len(p2Cards):
    print("Player 1 has",str(len(p1Cards)),"cards:")
    print("Player 2 has",str(len(p2Cards)),"cards:")
    print("\nPlayer 1 Wins the game with:")
    sortedCards = sorted(p1Cards)
    for i in range(len(p1Cards)):
        print(" ",sortedCards[i][0],sortedCards[i][1])
    scoreToWrite = (","+p1fname+"-"+str(len(p1Cards)))
else:
    print("Player 1 has",str(len(p1Cards)),"cards:")
    print("Player 2 has",str(len(p2Cards)),"cards:")
    print("\nPlayer 2 Wins the game with:")
    sortedCards = sorted(p2Cards)
    for i in range(len(p2Cards)):
        print(" ",sortedCards[i][0],sortedCards[i][1])
    scoreToWrite = (","+p2fname+"-"+str(len(p2Cards)))

#add to scores file
addFile = open("scores.txt","a")
addFile.write(scoreToWrite)
addFile.close()

#Retrieves and Sorts High Scores from scores file
readScores = open("scores.txt","r")
highScores = readScores.read()
readScores.close()
splitScores = highScores.split(",")
highScores = []
for i in range(len(splitScores)):
    splitScore = splitScores[i].split("-")
    partName = splitScore[0]
    partScore = splitScore[1]
    highScores.append([partScore,partName])
sortedHighScores = sorted(highScores, reverse=True)

#Displays Top 5 scores to user
print("\nHigh Scores:")
if len(highScores) < 5:
    scoreRange = len(highScores)
else:
    scoreRange = 5
for i in range(scoreRange):
    print(str(i+1)+")",sortedHighScores[i][1],"-",sortedHighScores[i][0])
