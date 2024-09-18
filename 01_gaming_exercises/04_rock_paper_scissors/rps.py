Rock, Paper, Scissors, Kennedy Spencer v0.1


























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

    # let cpu select choice at random
    # compare player choice to cpu choice 
    # print the results to the screen 
    # award point to winner and output results.
