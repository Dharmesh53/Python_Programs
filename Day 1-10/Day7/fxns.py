def printer(guess):
    for alpha in guess:
        print(alpha+" ",end="")
    print()

def equal(word,guess):
    i=0
    for x in word:
        if guess[i]!=x:
            return False
        i=i+1
    return True