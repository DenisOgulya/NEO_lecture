# key = 3
# alphabet
# for, if

def encode (message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    shipher = ""
    key = 3;

    message = message.upper()

    for letter in message:
        if letter in alpha:
            index = (alpha.find(letter) + key) % len(alpha)
            shipher += alpha[index]
        else:
            shipher += letter


    print(shipher)


encode('to be or not', 2)