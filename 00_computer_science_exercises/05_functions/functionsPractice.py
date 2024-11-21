#  Functions Practice, Kennedy Spencer, v0.2

import random 
 
def helloWorldMulti(): # FUNCTION SIGNATURE 
    """This function will output Hello, World! in a language the user choose. """ # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five
    # allow the user to select (input) a choice for the language.
    # print "Hello, World!" to screen in that language. 
    print("""Hello, the language(s) you have available are listed down below:\n  Arabic\n Creole\n Spanish\n """) 
    
    languageName = input ("Please select the language(s) you would like to learn.\n").lower() 

    if languageName == "arabic": 
        print("marhaban bialealami!\n")
    elif languageName == "creole": 
        print("Bonjou mond\n")
    elif languageName == "spanish":
        print("¡Hola Mundo!\n")
    else:
        print("Please select the options above!\n ") 

helloWorldMulti() # FUNCTION CALL 


# Function to Determine Even / Odd Numbers
argument1 = random.randint(-1000, 1000)

def isEven(argument1: int) -> bool: # Requires one ARGUMENT (argument1) and RETURNS a Boolean value. 
    """Determines if an integer value is even or odd."""
    if argument1 % 2 == 0: 
            return True 
    else:
         return False 
    
print(isEven(argument1))

# Function with Multiple Arguments
def canRideRollerCoaster(age: int, height: int) -> bool:
    if age > 10 and height > 4: 
        print("You can ride.\n")
        return True 
    else:
        print("You cannot ride.\n")
        return False
    
canRideRollerCoaster(4, 10) # Arguments must be passes in the same order as the function signature indicates.