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

#AMUSMENT PARK HEIGGHT CHECKER EXAMPLE
#Must be > min. height and < max. height to ride.

#When writing if-elif-else blocks check for the HIGHEST VALUE first when using > or >= 
if height >=6: 
     print("You're to tall enough to ride the Tea Cups!\n") 
elif height >= 3: 
     print("You're too tall to ride the Tea Cups! \n") 
else: # "oh, no, somethings wrong!" 
     print("Erorr, height not detected. Do not ride.\n") 


#When writing if-elif-else blocks check for the LOWEST VALUE first when using < or <=
if height <= 3: 
      print("You not tall enough to ride the roller coasters!\n")
elif height < 6:
    print("You're tall enought to ride the roller coaster !\n")
else: # " oh, no, somethings wrong!"
    print("Error, height not detected. Do not ride.\n")

# Create an if-elif-else block that checks for temperature.
# If the temperature is at least 100, print thats its too hot outside.
# If the temperature is at least 50 degrees but less than 100, print that recess is allowed.
# If the temperature is at less than 50 degrees but greater than 0, print that recess is in the gym.
# If no temperature is detected, print an error message.

if temperature >= 100:
    print("It's too hot outside, students cannot go to recess.\n")
elif temperature >= 50:
    print("It's cool enough to go outside.\n")
elif temperature > 0:
    print("Recess will be in the gym.\n")
else:
    print("Error detcting temperature.\n")