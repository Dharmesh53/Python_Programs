names = []
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines(70)

with open("./Input/Letters/starting_letter.txt") as letter_model:
    letter = letter_model.read()

for i in names:
    name = i[0:-1]
    new_letter = letter.replace("[name],", name)
    address = "./Output/ReadyToSend/" + name + ".txt"
    with open(address, mode='w') as sending:
        sending.write(new_letter)
