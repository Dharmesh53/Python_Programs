import core

again='yes'

while again=="yes":
    choice=str(input("Type 'encode' for encryption, 'decode' for decryption\n")).lower()
    
    word=str(input("Enter the line:\n"))
    
    if choice=='encode' :
        print(f"Here is the {choice}d text: "+core.encryption(word))
    elif(choice=='decode'):
        print(f"Here is the {choice}d text: "+core.decryption(word))
    else:
        print("invalid choice")
    again=str(input("do you want to end the program or run again?\n")).lower()
