import random
import string

def randomPassword(length,number = True,special_character = True):
    character = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    letters = character
    if number:
        letters+=numbers

    if special_character:
        letters+=special
    
    pwd = ""
    criteria = False
    has_number = False
    has_special_character = False

    while not criteria or len(pwd)<length:
        new_char = random.choice(letters)
        pwd+= new_char

        if new_char in numbers:
            has_number = True
        
        elif new_char in special:
            has_special_character = True
        
        criteria = True

        if number:
            criteria =has_number
        
        if special_character:
            criteria =has_special_character and criteria
        
    return pwd





length= int(input('Password length? '))
has_num = input('Do you want to have numbers(y/n)? ').lower()=='y'
has_special = input('Do you want to have special character(y/n)? ').lower()=='y'

Pass=randomPassword(length,has_num,has_special)
print(Pass)