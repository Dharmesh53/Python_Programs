def calculate(array):
    sum=0
    for i in array:
        sum+=i
    return sum

def result(mineSum,aiSum):
    if mineSum>20:
        print("your Lose")
    elif mineSum==20:
        print("You Win!")
    if aiSum>20:
        print("You Win!")
    elif aiSum==20:
        print("AI Win!")