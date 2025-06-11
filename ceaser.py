# key = 3
# alphabet
# for, if



alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(alpha))

message = "Bzrute is killer z!!!"

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