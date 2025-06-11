first_number = int(input('Input first number: '))
second_number = int(input("Input second number"))

lowest_number = min(first_number, second_number)

while not(first_number % lowest_number == 0 and second_number % lowest_number == 0):
    lowest_number -=1 
    
print(lowest_number)