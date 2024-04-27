import random
import string

def generate_password (min_len, num = True, special_characters = True):

    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    pwd=""
    characters = letters
    if num:
        characters += numbers
    if special_characters:
        characters += special

    meets_criteria = False
    has_numbers = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in numbers:
            has_numbers = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if num:
            meets_criteria = meets_criteria and has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimun length: "))
number = input("Do you want numbers (y/n)? : ") == "y"
special_char = input("Do you want special characters (y/n)? : ") == "y"

pwd= generate_password(min_length, number, special_char)
print("The generated password is:", pwd)