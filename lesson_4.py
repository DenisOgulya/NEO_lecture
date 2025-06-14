  
def convert_camel_to_case (key):
    res = ""    
    for i in key:
        if i.isupper():  
             res += "_" + i.lower()
        else:
            res += i
    return (res)
     

user_status = "userIsAutenticated"
converted_word = convert_camel_to_case(user_status)
print(converted_word) 
