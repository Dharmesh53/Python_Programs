import random
options=['Rock','Paper','Scissor']

user_choice=int(input("Enter your choice, 0 for Rock, 1 for Paper, 2 for Scissor \n"))
ai_choice=random.choice(options)

print("Computer:"+str(ai_choice))

if((user_choice==0 and ai_choice=='Scissor') or (user_choice==1 and ai_choice=='Rock') or (user_choice==2 and ai_choice=='Paper')):
    print("You won")
elif((user_choice==0 and ai_choice=='Rock') or (user_choice==1 and ai_choice=='Paper') or (user_choice==2 and ai_choice=='Scissor')):
    print("DRAW")
else:
    print("You lost")

