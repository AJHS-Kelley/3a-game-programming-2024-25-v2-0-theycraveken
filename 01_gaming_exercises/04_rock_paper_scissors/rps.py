# Rock, Paper, Scissors, Kennedy Spencer v0.1

# MODULE IMPORTS
import random 

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerName = "Kennedy" 
playerChoice = None 

# DATA STRUCTURES -- CPU 
cpuScore = 0
cpuChoice = None

# PLAYER NAME INOUT 
playerName = input("Please type your name and press enter.\n")
print(f"Hello{playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()

# .lower() can turn ALL input into lowercase.
# .upper() can turn ALL input into UPPERCASE.

if isCorrect == "yes": 
    print(f"ok {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Please type your name and press enter.\n")

# THE RULES using MULTI-LINE STRINGS
print(""""
Welcome to Rock, Paper, Scissors Robot!
It's Time to play Rock, Paper, Scissors!

You will play against the CPU. The first to score 3 points wins.
You will select from ROCK, PAPER, or SCISSORS.
The cpu will select ROCK, PAPER or SCISSORS at randoms. 
      
1. ROCK BEATS SCISSORS!
2. SCISSORS BEATS PAPER!
3. PAPER BEATS ROCK!
""") 

#Multi-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""" 
Anything in between the sets of a double quotes is just ignored.
If you need to write large comments, it's easier to use multi-line strings than 
putting a # in front of 15 different lines.
""" 

#MAIN GAME LOOP 
while playerScore < 5 and cpuScore < 5: 
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n") 
    playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors"
        playerChoice = input("Please enter rock, paper, or scissors and press eneter.\n").lower() 
         if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        print("You are not following directions. Please try again.\n")
        exit()
    print(f"You have chosen {playerChoice}.\n")
else: 
    print(f"You have chosen {playerChoice}.\n")
    
    
    
 # let cpu select choice at random 
    cpuChoice = random .randint(0, 2)    #randomly select 0, 1, 0r 2. 
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1: 
        cpuChoice = "scissors"
    elif cpuChoice == 2: 
        cpuChoice = "paper" 
    else: 
        print("Unable to determine CPU choice.\nPlease restart.\n")
        exit()
    #print(f"CPU Choice: {cpuChoice}") 


    # compare player choice to cpu choice 
    if playerChoice == "rock" and cpuChoice == "paper"
        pass
        #CPU WINS 
    elif playerChoice == "rock" and cpuChoice == "scissors"
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a ponit.\n")
        playerScore += 1  
        # PLAYER WINS 

    elif playerChoice == "rock"



    # print the results to the screen 
    # award point to winner and output results.
