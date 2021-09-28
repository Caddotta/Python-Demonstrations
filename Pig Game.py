import random
def Problem_0():
    dice_sides=[1,2,3,4,5,6]
    total=0
    PCTotalScore=0
    while total < 20:
        dice=random.choice(dice_sides)
        if dice > 1:
            total+=dice
            PCTotalScore+=total
        elif dice == 1:
            total=0
            return total
    return total

move=str('')

def Problem_Eight():
    playerselect=random.randint(1,2)
    dice_sides=[1,2,3,4,5,6]
    PCTotalScore=0
    UserTotalScore=0
    
    if playerselect==1:
        
        print('You are player 1'+'\n')
        #computer first then user
        
        while PCTotalScore<100 and UserTotalScore<100:
            
            total=0
            print('It\'s player 1\'s turn')
            move=str(input('Hold/Roll? (Enter) '))
            
            while len(move)>0 and move[0].upper()=='R':
                
                dice=random.choice(dice_sides)
                print(('Roll: ')+str(dice))
                
                if dice>1:
                    total+=dice
                    print('New Total: '+str(total)+'\n')
                    move=str(input('Hold/Roll? (Enter) '))
                elif dice==1:
                    total=0
                    move=str('')
                
            UserTotalScore+=total        
            print('\n'+'Turn Total: '+str(total))
            print('New Score: '+str(UserTotalScore)+'\n')
             
            total=0

            print('It\'s player 2\'s turn')
            while total<20 and PCTotalScore<100:
                
                dice=random.choice(dice_sides)
                
                print(('Roll: ')+str(dice))
                
                if dice>1:
                    total+=dice
                elif dice==1:
                    total=0
                    break
            PCTotalScore+=total    
            print('Turn total: '+str(total))
            print('New Score: '+str(PCTotalScore)+'\n')
            
            print('Player 1 Score: '+str(UserTotalScore))
            print('Player 2 Score: '+str(PCTotalScore)+'\n')
        
        #user first then computer


    elif playerselect==2:
        
        #computer first then user
        
        print('You are player 2')
        
        while PCTotalScore<100 and UserTotalScore<100:

            total=0

            print('It\'s player 1\'s turn')
            while total<20 and PCTotalScore<100:
                
                dice=random.choice(dice_sides)
                
                print(('Roll: ')+str(dice))
                
                if dice>1:
                    total+=dice
                elif dice==1:
                    total=0
                    break
            PCTotalScore+=total    
            print('Turn total: '+str(total))
            print('New Score: '+str(PCTotalScore)+'\n')
            
            print('Player 1 Score: '+str(PCTotalScore))
            print('Player 2 Score: '+str(UserTotalScore)+'\n')
        
            total=0
            print('It\'s player 2\'s turn')
            move=str(input('Hold/Roll? (Enter) '))
            
            while len(move)>0 and move[0].upper()=='R':
                
                dice=random.choice(dice_sides)
                print(('Roll: ')+str(dice))
                
                if dice>1:
                    total+=dice
                    print('New Total: '+str(total)+'\n')
                    move=str(input('Hold/Roll? (Enter) '))
                elif dice==1:
                    total=0
                    move=str(' ')
                
            UserTotalScore+=total        
            print('\n'+'Turn Total: '+str(total))
            print('New Score: '+str(UserTotalScore)+'\n')
            

Problem_Eight()
