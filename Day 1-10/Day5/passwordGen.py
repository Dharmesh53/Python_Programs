import random

symbol = ['!', '@', '#', '$', '%', '^', '&', '*']
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = int(input("Enter the no. of Digits: "))
symbols = int(input("Enter the no. of Symbols: "))
alpha = int(input("Enter the no. of Alphabet: "))
password = []

for i in range(1, numbers):
    password.append(random.randint(0, 9))
for i in range(1, symbols):
    password.append(symbol[(random.randint(0, 7))])
for i in range(1, alpha):
    password.append(random.choice(characters))

random.shuffle(password)

final = ""
for ch in password:
    final += str(ch)

print("Here is your very strong password: "+final)
