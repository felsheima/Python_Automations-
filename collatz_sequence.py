#A function that prints number // 2 if even, if odd then it prints 3 * number + 1.

def collatz (number):
    if number % 2 == 0:
        return (number // 2)
    else:
        return (3 * number + 1)
        
#User can type in an integer and keeps calling collatz until the funtion returns the value 1

user_input = int(input("Enter a number to throw into the collatz function: "))

while user_input != 1:
    user_input = collatz(user_input)
    print(user_input) 




