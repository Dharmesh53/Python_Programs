import random as rd


def generator():
    password = ""
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v',
             'w', 'x', 'y', 'z']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '/', ';', '?']

    for i in range(0, 15):
        idx = rd.randint(0, 3)
        if idx == 0:
            password = password + rd.choice(capital)
        elif idx == 1:
            password = password + rd.choice(small)
        elif idx == 2:
            password = password + rd.choice(number)
        else:
            password = password + rd.choice(special)

    return password
