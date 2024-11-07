# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

def displayIntro():

    print('You are on the moon with the aliens. In front of you,')
    print('you see two portal maps. In one map, you go to the army where its fun')
    print('and the people will treasure you with love. The other map')
    print('is full of slaves, and will eat you on sight.')
    print()

def chooseMap():
    map = ''
    while map != '1' and map != '2':
        print('Which map will you go choose? (1 or 2)')
        map = input()
    return map

def checkMap(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyMap = random.randint(1, 2)

    if chosenMap == str(friendlyMap):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    mapNumber = chooseMap()
    checkMap(caveMap)
    print('Do you want to play again? (yes or no)')
    playAgain = input()