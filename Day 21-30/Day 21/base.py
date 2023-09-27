# file = open("example.txt")
# content = file.read()
# print(content)
# file.close()

with open("example.txt", mode='r') as file:
    content = file.read()
    print(content)

with open("example.txt", mode='a') as file:
    file.write(", I gonna complete it.")
