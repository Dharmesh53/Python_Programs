alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


def encryption(word):
    output = ""
    for letter in word:
        position = alphabets.index(letter)
        newPos = (position+5) % 27
        output += alphabets[newPos]
    return output


def decryption(word):
    output = ""
    for letter in word:
        position = alphabets.index(letter)
        newPos = (position-5) % 27
        output += alphabets[newPos]
    return output
