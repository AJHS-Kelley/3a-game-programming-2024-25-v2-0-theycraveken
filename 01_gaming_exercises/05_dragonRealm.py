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
    print('is full of slaves, and will torcher and kill you.')
    print()

def chooseMap():
    map = ''
    while map != '1' and map != '2':
        print('Which map will you go choose? (1 or 2)')
        map = input()
        print(' If choose ')
    return map
    



def checkMap(map):
    if map == '1':
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

    friendlyMap = random.randint(1, 2)

    if map == str(friendlyMap):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')







playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    mapNumber = chooseMap()
    checkMap(mapNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()





    # CLOSE THE FILE
saveData.write('END OF GAME LOG\n\n') 
saveData.close()