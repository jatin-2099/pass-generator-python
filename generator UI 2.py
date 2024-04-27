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
    try:
        min_length = int(length_entry.get())
        if min_length <= 0:
            raise result_label.config(text="Minimum length must be a positive integer")
        else:
            result_label.config(text="")
    except ValueError:
        result_label.config(text="Invalid input for minimum length. Please enter a positive integer.")

    number = number_var.get()
    special_char = special_char_var.get()

    generated_password = generate_password(min_length, number, special_char)

    result_label.config(text="Generated Password: " + generated_password)

def create_widget_frame(parent, title):
    frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
    frame.pack(padx=10, pady=10)

    title_label = tk.Label(frame, text=title, font=("Helvetica", 14, "bold"))
    title_label.pack(padx=5, pady=5, anchor="center")

    return frame

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("720x480")

widget_frame = create_widget_frame(root, "Password Generator")

# Add widgets
length_label = ttk.Label(root, text="Minimum Length:")
length_label.pack(padx=5, pady=5)

length_entry = ttk.Entry(root)
length_entry.pack(padx=5, pady=5)

number_var = tk.BooleanVar()
number_checkbox = ttk.Checkbutton(root, text="Include Numbers", variable=number_var)
number_checkbox.pack(padx=5, pady=5)

special_char_var = tk.BooleanVar()
special_char_checkbox = ttk.Checkbutton(root, text="Include Special Characters", variable=special_char_var)
special_char_checkbox.pack(padx=5, pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password_and_display)
generate_button.pack(padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.pack(padx=5, pady=5)

# Start the main event loop
root.mainloop()