word = "hello,,, son,,, when you,,, are comming,,,,,, home,,,,,,,,,"

def dad_filter(message):
    while ",," in message:
        message = message.replace(",,",",").rstrip(",")
        
    return message

res = dad_filter(word)
print(res)