import random

class PasswordGenerator:
    def __init__(self, length):
        self.user_input = length 
        self.lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"
        self.special_chars = "!@#$%^&*"
        self.characters = self.lowercase + self.uppercase + self.numbers + self.special_chars
        
    def generate(self):
        password = ""
        
        for i in range(self.user_input):
            character = random.choice(self.characters) 
            password = password + character 

        return password

if __name__ == "__main__":
    length = int(input("How long would you like your password to be? :"))
    generator = PasswordGenerator(length)
    password = generator.generate()
    print("The password your generator created is: ",password)
