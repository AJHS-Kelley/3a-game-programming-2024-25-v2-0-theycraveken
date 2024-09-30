# Rock, Paper, Scissors, Kennedy Spencer v0.1

# MODULE IMPORTS
import random, time 

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerChoice = None 
numDraws = 0 

# DATA STRUCTURES -- CPU 
cpuScore = 0
cpuChoice = None

#MAIN GAME LOOP 
while playerScore < 5 and cpuScore < 5: 
  
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

  # let PLAYER select choice at random 
    playerChoice = random .randint(0, 2)    #randomly select 0, 1, 0r 2. 
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1: 
        playerChoice = "scissors"
    elif playerChoice == 2: 
        playerChoice = "paper" 
    else: 
        print("Unable to determine CPU choice.\nPlease restart.\n")
        exit()

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
