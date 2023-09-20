import random
import fxns
cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10,10]
mine=[]
ai=[]
again='yes'
mineSum=0
aiSum=0

mine.append(random.choice(cards))
ai.append(random.choice(cards))

while again=='yes': 
    mine.append(random.choice(cards))
    ai.append(random.choice(cards))
    mineSum=fxns.calculate(mine)
    aiSum=fxns.calculate(ai)
    print("your cards:" , mine)
    print("AI cards:" , ai[0])
    fxns.result(mineSum,aiSum)
    again=str(input("Do you want to continue, type 'yes' or 'no': \n")).lower()
    if again=='no':
        if mineSum>aiSum:
            print("You win!")
        else:
            print("You lose!")
