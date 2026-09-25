from password_generator import PasswordGenerator
import re

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password 

    def analyze(self):
        strong_length = len(self.password) > 12        
        uses_lowercase =  bool(re.search(r"[a-z]", self.password))
        uses_uppercase = bool(re.search(r"[A-Z]", self.password))
        uses_number = bool(re.search(r"[0-9]", self.password))
        uses_special_char = bool(re.search(r"[!@#$%^&*]", self.password))

        #Run the checks 
        if strong_length == True:
            print("Length = Strong")
        else:
            print("Length = Weak")
        if uses_lowercase == True:
            print("Lowercase = Strong")
        else:
            print("Lowercase = Weak")
        if uses_uppercase == True:
            print("Uppercase = Strong")
        else:
            print("Uppercase = Weak")
        if uses_number == True:
            print("Number = Strong")
        else:
            print("Number = Weak")
        if uses_special_char == True:
            print("Special character = Strong")
        else:
            print("Special character = Weak")

        #Determine overall strength
        overall_strength = strong_length and uses_lowercase and uses_uppercase and uses_number and uses_special_char 

        #Print the report
        print("\nPASSWORD SECURITY REPORT")
        print("------------------------")
        print(strong_length)
        print(uses_lowercase)
        print(uses_uppercase)
        print(uses_number)
        print(uses_special_char)
        print(overall_strength)
        
