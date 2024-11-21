# Rock, Paper, Scissors, Kennedy Spencer v3.3c

# MODULE IMPORTS
import random 

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerName = "Kennedy" 
playerChoice = None 

# DATA STRUCTURES -- CPU 
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT 
def playerName() -> str: # Function Singnature -- name of function, (arguments if any)
    """"Gets the name from the player and returns it."""
    # The line above is a DOCSTRING, it gives a breif example of what the function does.
    playerName = input("Please type your name and press enter.\n")
    print(f"Hello{playerName}!\n")
    isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()
    if isCorrect == "yes": 
        print(f"ok {playerName}, let's play Rock, Paper, Scissors!\n")
    else:
        playerName = input("Please type your name and press enter.\n")
    return playerName 

# THE RULES using MULTI-LINE STRINGS 
def rules() -> None: 
    """This function prints the rules for rock, paper, scissors."""
    print(f"""
    Welcome {playerName} to Rock, Paper, Scissors Robot!
    It's Time to play Rock, Paper, Scissors!

    You will play against the CPU. The first to score 5 points wins.
    You will select from ROCK, PAPER, or SCISSORS.
    The cpu will select ROCK, PAPER or SCISSORS at randoms. 
      
    1. ROCK BEATS SCISSORS!
    2. SCISSORS BEATS PAPER!
    3. PAPER BEATS ROCK!
    """) 
# Does another part of this program need to access this information?
# IF YES, YOU MUST HAVE A return STATEMENT
# IF NO, A return STATEMENT IS NOT REQUIRED

def playerChoice() -> str:
    """Allows the player to choose rock, paper, scissors."""
    playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper, or scissors and press eneter.\n").lower() 
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("You are not following directions. Please try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
    return playerChoice

def cpuChoice() -> str: 
    """Allows the CPU to choose rock, paper, scissors."""
    cpuChoice = random.randint(0, 2)    #randomly select 0, 1, 0r 2. 
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1: 
        cpuChoice = "scissors"
    elif cpuChoice == 2: 
        cpuChoice = "paper" 
    else: 
        print("Unable to determine CPU choice.\nPlease restart.\n")
        exit()
    return cpuChoice 
# Remove the lines of code that add score to player, CPU, or draws below.
def pickWinner(playerChoice: str, cpuChoice: str) -> str:
    """Determines the winner using player and CPU choices."""
    if playerChoice=="rock" and cpuChoice == "paper":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The Cpu wins a point.\n")
        return "CPU Wins"
    elif playerChoice == "rock" and cpuChoice == "scissors":
        # PLAYER WINS
        print(f" The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        return "Player Wins"
    elif playerChoice == "rock" and cpuChoice == "rock":
        # Draw
        print(f"The CPU chose {cpuChoice}and you chose {playerChoice}.\n")
        print("It's a draw!\n") 
        return "Draw"
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # CPU WINS  
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        return "CPU Wins"
    elif playerChoice == "scissors" and cpuChoice == "paper":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice}and you chose {playerChoice}.\n")
        print("you win a point.\n")
        return "Player Wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}. \n")
        print("It's a draw! \n")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "rock":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice}and you chose {playerChoice}. \n")
        print("You win a point. \n")
        return "Player Wins"
    elif playerChoice == "paper" and cpuChoice == "paper":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}. \n")
        print ("It's a draw! \n")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "scissors" :
        # CPU WINS
        print (f"The CPU chose {cpuChoice}and you chose {playerChoice}. \n")
        print ("The CPU wins a point. \n" )
        return "CPU Wins"
    else:
        print ("Unable to determine a winner. Please restart. \n")
        exit()

def score(winner: str) -> int:
    """This function uses the winner to update the score for CPU, Num. DRAWS, and player score."""
    if winner == "Player Wins":
        score = 1
    elif winner == "CPU Wins":
        score = 1 
    else: # This is a DRAW. 
        score = 0 
    return score 

def matchWinner(playerScore: int, cpuScore: int) -> bool:
    """This function determines if a player has won the game or not by scoring 5 points."""
    if playerScore >= 5:
        print("Congratulations! You are the winner.\n")
        return True 
    elif cpuScore >= 5:
        print("Sadly, you have been defeated by the CPU.\n")
        return True 
    else: #No winner yet.
        return False 
    
def playGame(playerScore: int, cpuScore: int) -> None:
    """This function will use all other functions to play Rock, Paper, Scissors. """
    while True:
        cpuPick = cpuChoice()
        playerPick = playerChoice()
        roundWinner = pickWinner(playerPick, cpuPick)
        if roundWinner == "Player Wins":
            playerScore += score(roundWinner)
        if roundWinner == "CPU Wins":
            cpuScore += score(roundWinner)

        print(f"Player Score: {playerScore}\n")
        print(f"CPU Score: {cpuScore}\n")

        if matchWinner(playerScore, cpuScore) == True:
            break

playGame(playerScore, cpuScore)