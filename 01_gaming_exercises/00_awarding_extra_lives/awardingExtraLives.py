# Awarding Extra Lives, Spencer, Kennedy, v0.0


lives = 3 
score = 50540 
name= "player"



# print(f"Hello {name}! You scared {score} points.\n")



# CHARACTER REFERENCE 
# CURLY BRACES {}
# ANGLE-BRACKETS<>
# PARENTHESIS ()


# Allow the user to input the score AS AN INTERGER 

# Allow the user to input the score. <-- MISSING THIS 

# If score is 10000 or less
    # Lose a life
# Else score is > 10000 but less than 100001 

    # Give 1 Extra Life 
# If score is > 100000 
    #Give 2 Extra Lives 

# Output the score and number of lives to the screen.  

if score <= 10000: 
    print("You will not continue and will lose 1 life!\n")
    #lives = lives - 1 
    lives -= 1 
elif score < 100001:
    print("You're eligile to continue and an extra life will be added!\n") 
    lives += 1 
else: # " oh, no, somethings wrong!"
    print("Error, score not detected. Do not continue.\n")
    lives += 2

print(f"Greetings {name}! You have {lives} remaining after scoring {score} points.\n")
