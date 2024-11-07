# Dragon Realm, <Kennedy Spencer>, v0.1
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

def displayIntro():

    print('You are on the moon with the aliens. In front of you,')
    print('you see two portal maps. In one map, you go to the army where its fun')
    print('and the people will treasure you with love. The other map Ancient')
    print('is full of slaves, and will torcher and kill you.')
    print()

def chooseMap():
    map = ''
    while map1 != '1' and map2 != '2':
        print('Which map will you go choose? (1 or 2)')
        map = input()
    return map

map1 = 'Army' 
map2 = 'Ancient'

def checkMap(Army):
    print('You approach the Army...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyMap = random.randint(1, 2)

    if Army == str(friendlyMap):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')

def checkMap(Ancient):
    print('You enter the Ancient...')
    time.sleep(2)





playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    mapNumber = chooseMap()
    checkMap(mapNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()