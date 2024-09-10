# Flow Control Structures, Kennedy Spencer, v0.0
# Making Computer Programs Make Decisions

temperature = 5.43
color = "Orange"
height = 5 
likesPineappleOnPizza = False 

# SINGLE DECISION POINT - if statment 
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISON OPERATOR 99% of this time.
    #runThisCode IF the CONDITION_EXPRESSION is True 

if temperature > 100: 
    print("It is hot as the sun outside.\n") 
    
if height < 7: 
    print("You are tiny. \n") 
 
# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likesPineappleOnPizza: 
    print("Yummy") 

# What if we want something different to happen?
if color  == "Black": # COMMON ERROR FOR STUDENTS IS USING = instead of ==.
    print("Your shirt is the correct uniform color.\n") 
else: 
    print("Your shirt is not the correct uniform color.\n") 

carSpeed = 65 
if carSpeed <78: 
    print("Your going to fast.\n") 