import random,art

print(art.logo)
print("Welcome to The Number Guessing Game\nI'm thinking of a number between 1 to 100")
mode=str(input("Choose the difficulty level (EASY or HARD): ")).lower()

if mode=="easy":
    attempts=10
else:
    attempts=5

NUMBER=random.randint(0,100);

while attempts>0:
    print(f"You have {attempts} remaining to guess the number")
    guess=int(input("Make a guess: "))
    if guess>NUMBER:
        print("TOO HIGH")
    elif guess<NUMBER:
        print("TOO LOW")
    else:
        print("BOOM BABY YOU GOT IT RIGHT")
        break;
    
    attempts=attempts-1

if(attempts==0 and guess!=NUMBER):
    print("YOU LOST BITCH, TRY AGAIN!!!")
    print(f"THE NUMBER WAS {NUMBER}")
else:
    print("YOU WON!!!")