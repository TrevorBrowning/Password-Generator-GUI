import random
from tkinter import *
import string 
import os
import sys
import time
import csv
from tkinter import messagebox





def generate_password():
    char_list = []
    char_pool = ''
    gen_pass = ''

    if lowercase_char.get():
        char_pool += string.ascii_lowercase

    if uppercase_char.get():
        char_pool += string.ascii_uppercase
    
    if symbols_char.get():
        char_pool += string.punctuation

    if numbers_char.get():
        char_pool += string.digits
    
    if not char_pool:
        pass_generated.config(text='Error. Please select a checkbox')

    password = ''

    for i in range(password_length.get()):
        password += random.choice(char_pool)
    
    
    pass_generated.config(text=password)
    strength_calc()
    save_txt_button.config(state=ACTIVE)
    save_csv_button.config(state=ACTIVE)
    
    


def copy_clipoard():
    
    password = pass_generated.cget('text')
    window.clipboard_clear()

    if len(password) > 0:
        window.clipboard_append(password)

    return password



def open_saved_folder():
    base_dir = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))
    )
    os.startfile(base_dir)



def save_passwords_txt():
    password = pass_generated.cget('text')
    timestamp = time.strftime("%m-%d-%Y %H:%M:%S")

    base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__)))

    file_path = os.path.join(base_dir, "Saved_Passwords.txt")

    with open(file_path, "a") as file:
        file.write(f"[{timestamp}] {password}\n")

import csv  # Add this at the top of your script

def save_passwords_csv():
    password = pass_generated.cget('text')
    timestamp = time.strftime("%m-%d-%Y %H:%M:%S")

    base_dir = getattr(
        sys, '_MEIPASS',
        os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))
    )
    file_path = os.path.join(base_dir, "Saved_Passwords.csv")

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, password])





def clear_saved_passwords():
    confirm = messagebox.askyesno("Clear Saved Passwords", "Are you sure you want to delete all saved passwords? (No undo)")
    if confirm:
        base_dir = getattr(
            sys, '_MEIPASS',
            os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))
        )

        txt_path = os.path.join(base_dir, "Saved_Passwords.txt")
        csv_path = os.path.join(base_dir, "Saved_Passwords.csv")

        with open(txt_path, "w") as file:
            pass 

        with open(csv_path, "w", newline="") as file:
            pass 


def strength_calc():
    password = pass_generated.cget('text')
    score = 0
    
   
    
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1   
    if any(c.isdigit() for c in password): score += 1        
    if any(c in string.punctuation for c in password): score += 1  
    if len(password) >= 12: score += 1

    if score <= 2:
        strength_label.config(bg='yellow', text='Weak')
    
    elif score <= 4:
        strength_label.config(bg='green', text='Medium')
    
    else:
        strength_label.config(bg='red', text='Strong')
    
    score = 0



window = Tk()
window.grid_columnconfigure(0, weight=1)

password_length = IntVar()
lowercase_char = BooleanVar()
uppercase_char = BooleanVar()
symbols_char = BooleanVar()
numbers_char = BooleanVar()

window.geometry("600x470")
window.eval('tk::PlaceWindow . center')
window.configure(bg='darkgrey')
window.title('Password Generator')
window.resizable(False, False)
window.iconbitmap("icon.ico")





body_frame = Frame(window, bd=2, relief=RAISED)
body_frame.grid(padx=20, pady=(20,40), sticky='n')
body_frame.grid_columnconfigure(0, weight=1)
body_frame.grid_columnconfigure(1, weight=1)
body_frame.grid_columnconfigure(2, weight=1)
body_frame.grid_columnconfigure(3, weight=1)



config_frame = LabelFrame(body_frame, text="Config", font=('Ariel', 12), bg='lightgrey')
config_frame.grid(row=3, column=0, rowspan=7, padx=(10, 10), pady=(10,10), sticky='nw')

pass_len_label = Label(config_frame, text='Pass Length', font=('Ariel', 12), bg='lightgrey')
pass_len_label.grid(row=0, column=0, sticky='w')

pass_len_slider = Scale(config_frame, from_=6, to=32, orient=HORIZONTAL, variable=password_length, font=('Ariel', 12), bg='lightgrey', troughcolor='lightgrey')
pass_len_slider.grid(row=1, column=0, columnspan=2, sticky='w')

lower_check = Checkbutton(config_frame, text='Lowercase', font=('Ariel', 12), variable=lowercase_char, bg='lightgrey')
lower_check.grid(row=2, column=0, sticky='w')

upper_check = Checkbutton(config_frame, text='Uppercase', font=('Ariel', 12), variable=uppercase_char, bg='lightgrey')
upper_check.grid(row=3, column=0, sticky='w')

digit_check = Checkbutton(config_frame, text='Numbers', font=('Ariel', 12), variable=numbers_char, bg='lightgrey')
digit_check.grid(row=4, column=0, sticky='w')

symbol_check = Checkbutton(config_frame, text='Symbols', font=('Ariel', 12), variable=symbols_char, bg='lightgrey')
symbol_check.grid(row=5, column=0, sticky='w')

gen_button = Button(config_frame, text='Generate', font=('Ariel', 12), command=generate_password)
gen_button.grid(row=6, column=0, pady=(10, 10), padx=(15,0), sticky='w')





tools_frame = LabelFrame(body_frame, text="Tools", font=('Ariel', 12), bg='lightgrey')
tools_frame.grid(row=4, column=1, rowspan=6, padx=(20, 0), sticky='ne')

save_txt_button = Button(tools_frame, text='Save .txt', font=('Ariel', 12), command=save_passwords_txt, width=15, state=DISABLED)
save_txt_button.grid(row=0, column=0, pady=(5, 5))

save_csv_button = Button(tools_frame, text='Save .csv', font=('Ariel', 12), width=15, state=DISABLED, command=save_passwords_csv)
save_csv_button.grid(row=1, column=0, pady=(5, 5))

clear_button = Button(tools_frame, text='Clear Saved', font=('Ariel', 12), width=15, command=clear_saved_passwords)
clear_button.grid(row=2, column=0, pady=(5, 5))

view_button = Button(tools_frame, text='View Saved List', font=('Ariel', 12), width=15, command=open_saved_folder)
view_button.grid(row=3, column=0, pady=(5, 5))



password_display_frame = LabelFrame(body_frame, text="Output", font=('Ariel', 12))
password_display_frame.grid(row=11, column=0, columnspan=4, sticky="ew", pady=(20, 10), padx=(10,20))


password_display_frame.grid_columnconfigure(0, weight=0)
password_display_frame.grid_columnconfigure(1, weight=1)
password_display_frame.grid_columnconfigure(2, weight=0)
password_display_frame.grid_columnconfigure(3, weight=0)

pass_gen_label = Label(password_display_frame, text='Password:', font=('Ariel', 12))
pass_gen_label.grid(row=0, column=0, sticky='e', padx=(5, 5), pady=(10, 5))

pass_generated = Label(password_display_frame, text='', font=('Ariel', 14), bg='lightgrey',
                       width=40, relief=SUNKEN, anchor="center")
pass_generated.grid(row=0, column=1, columnspan=2, sticky='ew', pady=(10, 5), padx=(0, 5))

copy_button = Button(password_display_frame, text='Copy', font=('Ariel', 12), command=copy_clipoard)
copy_button.grid(row=0, column=3, padx=(0, 5))


strength_text = Label(password_display_frame, text='Strength:', font=('Ariel', 12))
strength_text.grid(row=1, column=0, sticky='ew', padx=(10, 5), pady=(10, 15))

strength_label = Label(password_display_frame, text='', font=('Ariel', 12), relief=SUNKEN,
                       width=40, bd=2, anchor="center")
strength_label.grid(row=1, column=1, columnspan=2, sticky='ew', pady=(0, 15), padx=(0, 5))




window.mainloop()