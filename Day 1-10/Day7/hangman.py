import random
import fxns
import asciiArt

words=['beekeeper']
# words=['beekeeper','cowboy','beeboop','lighting','jbl','whitebeard']
word=random.choice(words)

guess=[]
for i in range(len(word)):
    guess.append("_")
fxns.printer(guess)

idx=0
while not fxns.equal(word,guess) and idx!=7:
    letter=str(input("Guess a word to save the hangman:\n"))
    i=0
    flag=False

    for x in word:
        if letter==x:
            flag=True
            guess[i]=x
        i=i+1
    if flag==False:
        print(asciiArt.hangman[idx])
        idx=idx+1
    
    fxns.printer(guess)