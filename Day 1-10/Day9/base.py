import os
from time import sleep

bids={}
again='yes'
maxi=0

while again=='yes':
    name=str(input("Please enter your name: ")).capitalize()
    bid=int(input("Enter your bid: "))
    bids[bid]=name
    again=str(input("Is there anyone who want to bid!! Type 'Yes' or 'No' \n")).lower()
    if(again=='yes'):
        os.system('cls')
    else:
        for x in bids:
            if int(x)>maxi:
                maxi=x
    
print(f"The winner of the Auction is {bids[maxi]}")