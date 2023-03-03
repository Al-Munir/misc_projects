#Description: Generate a random password using Python

import string
import random

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

while True:
    pass_len = int(input('What length would you like your password to be:'))
    
    password = ""
    
    for x in range(0,pass_len):
        password_char = random.choice(chars)
        password = password + password_char
    
    print('Here is your password:', password)

    