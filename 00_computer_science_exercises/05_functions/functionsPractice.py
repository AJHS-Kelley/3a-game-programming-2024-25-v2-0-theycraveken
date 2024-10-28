#  Functions Practice, Kennedy Spencer, v0.1

import random 
 
def helloWorldMulti(): # FUNCTION SIGNATURE 
    """This function will output Hello, World! in a language the user choose. """ # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five
    # allow the user to select (input) a choice for the language.
    # print "Hello, World!" to screen in that language. 
    print("""Hello, the language(s) you have available are listed down below: Arabic\n Creole\n Spanish\n """) 
    
    languageName = input ("Please select the language(s) you would like to learn.\n") 

    if languageName == "Arabic": 
        print("marhaban bialealami!\n")
    if languageName == "Creole": 
        print("Bonjou mond\n")
    if languageName == "Spanish":
