import random
import string
import tkinter as tk
from tkinter import ttk

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

def generate_password_and_display():
    min_length = int(length_entry.get())
    number = number_var.get()
    special_char = special_char_var.get()

    generated_password = generate_password(min_length, number, special_char)

    result_label.config(text="Generated Password: " + generated_password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Add widgets
length_label = ttk.Label(root, text="Minimum Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

number_var = tk.BooleanVar()
number_checkbox = ttk.Checkbutton(root, text="Include Numbers", variable=number_var)
number_checkbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

special_char_var = tk.BooleanVar()
special_char_checkbox = ttk.Checkbutton(root, text="Include Special Characters", variable=special_char_var)
special_char_checkbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

generate_button = ttk.Button(root, text="Generate Password", command=generate_password_and_display)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the main event loop
root.mainloop()