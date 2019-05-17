# Write a function that uses regular expressions to make sure the password string it is passed is strong. 
# A strong password is defined as one that is at least eight characters long, 
# contains both uppercase and lowercase characters, 
# and has at least one digit. 
# You may need to test the string against multiple regex patterns to validate its strength.

import re

def password_strength():
    text = input('Enter your password: ')
    
    password_requirements = re.compile(r'[A-Z]+[a-z]+[0-9]+')
    mo = password_requirements.search(text).group()
    print(mo)

password_strength()