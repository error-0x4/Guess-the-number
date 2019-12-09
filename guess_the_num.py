import random

n = random.randint(1, 100)
win = False
count = 0

while win == False:
    ch = int(input('enter your answer'))
    count += 1
    print('chances count = ', count, '\n')
    if ch == n:
        print('you win, thanks for playing')
        win = True
    elif ch < n:
        print('your choice ', ch ,'is less then the number')
    elif ch > n:
        print('your choice ', ch ,'is more then the number')

##    if(count >=6):
##        print("Game over!")
##        break;
    
    

