# Dragon Realm, <Kennedy Spencer>, v0.1
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time
import datetime

# SAVONG DATA TO A FILE 
# STEP 1 -- creating the file name to use.

logFileName = 'dragonRealmLog.txt'
# Example: dragonRealmLog1132AM.txt 

# Step 2 -- Create/ open the file to save the data 
saveData = open(logFileName, 'a')
# FILE MODES
# 'x' Creates file, if file exist, exit with erroe message.
# 'w' Creates file, if file exist, erase and overwrite file contents.
# 'a' Creates file, if file exists, append data to the file.

saveData.write('GAME STARTED' + ' ' + str(datetime.datetime.now()) + '\n')


def displayIntro():

    print('You are on the moon with the aliens. In front of you,')
    print('you see two portal maps. In one map, you go to the army where its fun')
    print('and the people will treasure you with love. The other map Ancient')
    print('is full of slaves, and will torcher and kill you... you may have an option to escape.')
    print()

def chooseMap():
    map = ''
    while map != '1' and map != '2':
        print('Choose if you dare....\n ')
        print('{1} You will teleport to the Army!\n {2} You will teleport to the Ancient world\n')
        print('Which map will you go choose? (1 or 2)')
        print('Insert the number of your desired map and press GO.\n')
        map = input()
    return map
    
def checkMap(map):
    
    if map == '1':
        saveData.write('Player choose the Army')
        print('Excellent choice my friend!....')
        time.sleep(2)
        print('You\'re entering the Army......')
        time.sleep(2)
    elif map == '2':
        print('Interesting choice my friend.....')
        time.sleep(2)
        print('I see you like to suffer...')
        time.sleep(2)
        print('lets see if you can escape!')
    else: 
            input('Please enter a valid number in order to continue.\n')
    return map


def chooseitems():
    items = ''
    while items != '11' and items != '21' and items != '31' and items != '41':
        print('You may need some items to get you through your journey...')
        print('{11} For the Army you can choose a Teddy Bear.\n{21} You may choose a toiletries.\n{31} You can choose a sword for Anicent.\n{41} You can choose Bomb.\n')
        print('Pick your choices wisley......')
        print('Which item will you choose? (11, 21, 31, 0r 41)')
        print('Insert the number of your desired item and press play.\n')
        items = input()
    return items

def checkitems(items): 

    if items == '11':
        print('You have choosen the Teddy bear.')
        time.sleep(2)
        print('The Teddy Bear is your bestfriend that comes to life in your alone time')
        print('As your in the Army getting all the love and all the fun you can get, the Teddy Bear is a life long partner that grants all your wishes!')
        time.sleep(2)
    elif items == '21':
        print('You have choosen the Toiletries')
        time.sleep(2)
        print('The toileties bag is a potion to always make you look nice.')
        print('Being that you will always look nice and can choose your style the people will love you unconditionally and will treat you like a King or Queen 4 Life!')
        time.sleep(2)
    elif items == '31':
        print('You have chosen a Sword for the Anicent World.')
        time.sleep(2)
        print('You will need to sword to kill the slaves and guards in a timely manner.')
        print('If you can defeat all the slaves and guards in time you WIN and can escape!')
        time.sleep(2)
        print('If not you loose and will be killed!')
    elif items == '41':
        print('You have choosen The Bomb!')
        time.sleep(2)
        print('For the Bomb you will have to find a nice place to plant it with our getting caught...')
        print('If you plant the bomb in time you WIN and can escape.')
        print('If you fail to plant the bomb in a timely manner or get caught you loose and will be killed!')
    else:
        input('Please enter a valid number\n')
    return items  




# I TRIED I GOT REALLY CONFUSED BUT I THINK I DID IT SOMEWHAT CORRECT!




playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    mapNumber = chooseMap()
    print(mapNumber)
    checkMap(mapNumber)
    items = chooseitems()
    checkitems(items)
    print('Do you want to play again? (yes or no)')
    playAgain = input()





    # CLOSE THE FILE
saveData.write('END OF GAME LOG\n\n') 
saveData.close()