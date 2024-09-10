# Data Types and Operators, Kennedy Spencer, v0.4

# Fundamental Data Types
# String - str - Sequence of letters, numbers, spaces, or other characters.
# Strings in python are inside ' ' or " "
# idc if you use ' ' or " " just be consistent.

# Boolean - bool - True or False values.

# Float - float - any number value with a decimal, +/-, including 0.0

# Intergers- int - any whole number, +/-, including 0.

# Data types are stored in VARIBLES.
# A varible is basically a bucket with a name to put into.
# VARIBLE  NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT!
# VARIBLES CANNOT START WITH A NUMBER
# camelCaseVaribleNames
# snake_case_varible_name

# DECLARING VARIBLES AND ASSIGNING VALUES 

highScore = 5648971 # int data types 

carSpeed = 9.1126 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple= False  # boolean data type 

playerName = "theycraveken" # string data name
backgroundColor = "Black" # string data type 

# ASSIGN NEW VALUES
playerName = "Lloyd Spencer" 
carSpeed = -5.41 

# DATA TYPES CAN CHANGE, BE CAREFUL 
hasAxe = 2.3 

# Printing Data Types
newInt = 4
newFloat = 2.1 
newString = "twinkletoes"
newBool= False 

print(type(newInt)) 
print(type(newFloat)) 
print(type(newString)) 
print(type(newBool)) 

# printing Varible to console / Screen
# print(playerName) 
# print(isPurple)
# print(carSpeed)
# print(backgroundColor) 

# printing varibles and expressions to counsole / screen 
# print(highScore + 999)
# print(33 * 2)
# print(carSpeed) 


# PRINTING VARIBLES INSIDE OF STRINGS 
# print(f"Hey {playerName}. You Did It! Your High Score is {highScore}.\n") 

# ARITHMETIC OPERATIONS 
myInt = 8
myFloat = 4.21
myNum = 0 


# addition
inInt = 5 + 6 
myFloat = 7.4 + 2.11 


myInt = myInt + 3 

myNum = myInt + myFloat 
# When you add an int and a float together, the answer becomes a float


# subtraction
myNum = myInt - myFloat 
myInt = myFloat - 1.23 

#Multiplication 
myNum = myInt * myFloat 

#Division 
myNumber = myInt / myFloat # first is numerator, second num is denominator  

#MODULUS (MODULO) % -- Returns REMAINDER after dividing. 
# MOST COMMON USE FOR MODULUS IS DETERMINING EVENN / ODD NUMBERS.
numStudents = 4 
numSlicesPizza = 16 

leftOvers = numSlicesPizza % numStudents 
print(leftOvers) 

# EXPONENTS **
numSquared = 4 ** 3 # 4 is the base, 3 is the exponent.

#FLOOR-DIVISION // Divides, throws out any decimal. 
myNum = myInt // myFloat 

# Addition-Assignment Operator - Mostly used for counters. 
myNum = 3 
myNum = myNum + 1 #Old-School Method 
myNum += 1 # New Hotness 
myNum *= 1 
myNum /= 1 


# COMPARISON OPERATORS 
## IS-EUQAL-TO -- Are the two values equal to eachother? 
# Returns True or False based o evaluation. 
x = 12.0
# print(x==5) 

# NOT-EQUAL-TO !== Are the two values NOT equal?
# Returns True or False based on evaluation.
# print(x != 12) 

# GREATER THAN / GREATER-THAN-OR-EQUAL TO 
# print(5 > 3) #Greater Than
# print(12 >= 2) # Greater Than or Equal to 

# LESS THAN / LESS-THAN-OR-EQUAL TO 
# print(5 < 3) #LESS Than
# print(12 <= 2) # Less Than or Equal to 

# LOGICAL OPERATIONS 
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE 
age = 34
height = 45 
eyeColor = "orange" 
# In order to ride the Teacups, you must be at least 18 years old and at least 58" tall.
print(age >= 18 and height >= 58) 
print(age >= 18 and height >= 58 and eyeColor == "Purple") 
# ALWAYS CHECK FOR THE LEAST-LIKELY TO BE FALSE CONDITION FIRST!!!!! 
#print(defeatedBoss == True and level > 5 and hasBlueKey == True) 

# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
print(age >= 18 and height >= 58) 
print(age >= 18 and height >= 58 and eyeColor == "Purple") 
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!! 
#print(defeatedBoss == False or level > 5 or hasBlueKey == True) 

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT. 
a = 8
print(a == 8)
print(not (not (a == 8)))

#COMBINING LOGICAL OPERATORS 
# print(a == 8 and hasKey -- True or isCloud == True)
# TRUE and 

# IDENTITY OPERATIONS 
g = 1.0 
h = 1.0 
i = g 
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g) 

# MEMBERSHIP OPERATORS 
fruits = {"apple", "banana", "tomato"}
print("banana" in fruits) 
print("potato" in fruits)
      
time = 13.25
temperature = 105
print(time > 13.25 and temperature < 120)
