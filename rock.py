import random

def game():

    user=input("enter your choice(rock/paper/scissor):")
    if (user.lower()=='rock')| (user.lower()=='paper')| (user.lower()=='scissor'):
        num='YES'
    else:
         print("invalid option!!")
         game()
    
    mm= ['rock' , 'paper', 'scissor']
    computer=random.choice(mm)
    while num=='YES':
        if user.lower()==computer:
              print("its a tie!!")
        elif (user.lower()=='rock') & (computer=='paper') |((user.lower()=='paper')&(computer=='scissor')) | (user.lower()=='scissor') & (computer=='rock') :
             print(f"you lose computer chose {computer}")
        else:
              print(f"you won computer chose {computer}")
        num=input("do you want to play again?(yes/no):")
        if (num=='yes' ) | (num=='no'):
             if num.upper()=='YES':
                  game()
             elif num.upper()=='NO':
                  break
                
        else:
              print("invalid option terminating the code!!")
game()

       
    