# -*- coding: utf-8 -*-


import pyperclip
import random

# Set the character list for generating the password
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"


# Generate strong password of at least 12 charachter length. Prompt user to re-enter length if under 12 characters.
def passGen():
    # Take the length of the password from the user
    password_length = int(input('Enter the length of the password: '))
    while True: 
        ## Set the minimum password length to 12 characters
        if password_length >= 12:
            # Generate the password
            password = "".join(random.sample(characters, password_length))
            # Print the generated password
            print("Gernerated password: %s" %password)
            break
        else:            
            ### Under 12 characters error message
            print('Strong passwords must be at least 12 characters long.')
            ### Repeat function to allow user to enter a higher length
            passGen()
            break

passGen()