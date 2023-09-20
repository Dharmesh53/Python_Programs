print('''
******************************************************************************************************
                                    Welcome to Treasure Island
******************************************************************************************************
''')
#TODO:replace it with ascii art.com

print("Your mission is to find the teasure.\n")
dir=str(input("You are at the cross road.where do you want to go ? Type 'Left' or 'Right'\n "))
if dir.lower()=="left":
    lake=str(input("You came to an Lake. You want to 'Swim' across the lake or 'Wait' for the boat?\n"))
    if lake.lower()=="wait":
        door=str(input("You came to an house.There are three door in which door you want to go 'Red','Black' and 'Blue'?\n")).lower()
        if door=="red":
            print("Game over MotherFucker,you choose to go in Room of Gays\n")
        elif door=="blue":
            print("Game over MotherFucker,you choose to go in Room of LGBTQ\n")
        else:
            print("You Win,you choose to go in Room of Hentai Womens\n")
    else:
        print("Game over MotherFucker,you got eaten by crocodiles\n")
else:
    print("Game over MotherFucker,you got the wrong way!!\n")
