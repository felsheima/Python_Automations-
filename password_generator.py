import random

user_input = int(input("How long would you like your password to be? :"))

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_chars = "!@#$%^&*"

characters = lowercase + uppercase + numbers + special_chars

password = ""

for i in range(user_input):
    character = random.choice(characters) 
    password = password + character 

print(password) 
