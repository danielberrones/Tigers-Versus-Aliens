from time import sleep

def alienRoom():
    '''this is the alien room'''
    print('this is the alien room')

def tigerRoom():
    '''this is the tiger room'''
    areTigersSleeping = True
    print('You open the door')
    sleep(3)
    print('There are 2 tigers sleeping in the corner.')
    sleep(2)
    print('What do you want to do?')
    print('Do you want to wake the tigers?')

    userChoice = input('> ')
    if 'yes' in userChoice:
        areTigersSleeping = False
        gameOver('The tigers killed you')

def gameOver(whatHappened):
    '''returns game over phrase'''
    print(f'{whatHappened}, Goodbye!')

def startGame():
    '''starts the game'''
    print('You enter a dark hallway but see two doors.')
    sleep(3)
    print('The left door says, "ALIENS MAY LIVE HERE"')
    print('The right door says, "TIGERS MAY LIVE HERE"')
    sleep(2)
    print('Which door?')

    firstDoor = input('> ')
    if 'left' in firstDoor:
        alienRoom()
    elif 'right' in firstDoor:
        tigerRoom()
    else:
        gameOver('Your response could not be understood.  Goodbye')

startGame()
