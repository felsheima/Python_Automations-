#Function that uses regular expressions to make sure the password string it is passed is strong. Atleast 8 characters, contains both upper and lowercase. and has atleast 1 digit.

import re

def strong_pass (password):
    if len(password) < 8:
        return False
    elif not re.search(r"\d", password):
        return False
    elif not re.search(r"[A-Z]", password):
        return False
    elif not re.search(r"[a-z]", password):
        return False
    else:
        return True

print(strong_pass("$H9gsO%*2ZqFit2QNDSU"))
print(strong_pass("bEQh0sWstz78UvVRF^p&"))
print(strong_pass("!kH7nSz&I1K5loh&Wq%B"))
print(strong_pass("catsruleanddogsdrool"))
