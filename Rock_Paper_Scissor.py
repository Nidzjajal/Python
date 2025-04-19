import random , sys

print('Rock, Paper , Scissors')

win=0
loss=0
tie=0

while True:
    print('%s Win , %s Loss , %s Tie' %(win , loss, tie))
    while True:
        print('Enter your move :Rock (r) , Paper (p) , Scissors (s) or Quit (q)')
        move =input()
        if move=='q':
            sys.exit()
        if move=='r' or move=='p' or move =='s' :
            break
        print('Type one of r,p,s or q')


    if move =='r':
        print('Rock versus...')
    elif move =='p':
        print('Paper versus....')
    elif move == 's' :
        print('Scissors versus...')

    ran=random.randint(1,3)
    if ran==1:
        com_move='r'
        print('Rock')
    elif ran==2:
        com_move='p'
        print('Paper')
    elif ran==3:
        com_move='s'
        print('Scissors')

    if move== com_move:
        print('it is a tie !')
        tie+=1
    elif move == 'r' and com_move=='s':
        print('You win !')
        win +=1
    elif move == 'p' and com_move=='r':
        print('You win !')
        win +=1
    elif move == 's' and com_move=='p':
        print('You win !')
        win +=1
    elif move == 'r' and com_move=='p':
        print('You Lose !')
        loss +=1
    elif move == 'p' and com_move=='s':
        print('You Lose !')
        loss +=1
    elif move == 's' and com_move=='r':
        print('You Lose !')
        loss +=1
        
        
        
        