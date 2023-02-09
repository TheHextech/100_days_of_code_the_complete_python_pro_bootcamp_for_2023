from tkinter import *
from tkinter import messagebox
import string
import numpy as np 
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    
    """This function generate a random password composed by 4 lowercase letters, 4 uppercase letters, 
    2 numbers and 2 special characters. Also, thanks to pyperclip, the password is copied in clipboard."""

    # Delete the entry (for older passwords)
    password_entry.delete(0, END)

    # Create array of lowercase letters and get 4 of them randomly 
    list_lower = np.array(list(string.ascii_lowercase))
    random_lower = np.random.choice(list_lower, size=4)

    # Create array of uppercase letters and get 4 of them randomly
    list_upper = np.array(list(string.ascii_uppercase))
    random_upper = np.random.choice(list_upper, size=4)

    # Create array of numbers and get 2 of them randomly
    list_number = np.arange(10)
    random_number = np.random.choice(list_number, size=2)

    # Create array of special characters and get 2 of them randomly
    spec_char = np.array(list("!@#$%&*()-_+={}[]\/^~<>?"))
    random_char = np.random.choice(spec_char, size=2)

    # Concatenate the arrays and shuffle them with a permutation
    concat_random = np.concatenate([random_char, random_number, random_lower, random_upper])
    concat_random_shuffled = concat_random[np.random.permutation(len(concat_random))]

    # Convert random shuffled array into a string and insert it into the password entry, also copy into the clipboard
    random_password = "".join(concat_random_shuffled)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    """This function get the text in website, username and password entries and store them in a txt file named 
    'Password container.txt'. If any of the entries is empty an error is displayed and the user is not allowed to
    proceed. Furthermore, when the 'Add' button is clicked it appears a messagebox where the user can confirm or cancel."""
    
    website = site_entry.get()
    username = user_entry.get()
    psw  = password_entry.get()

    # If any of these fields is empty an error popup is displayed
    if website == '' or username == '' or psw == '':
        messagebox.showerror(title='Missing fields', message='You must fill all fields before proceeding!')

    else:
        text = f"Site: {website}\nUsername: {username}\nPassword: {psw}\n\n"

        # The "Ok" is equal to a True
        is_ok = messagebox.askokcancel(title=website, message=f'{text}\nIt is ok to save?')

        if is_ok:
            # Write the credentials, reset the entries and focus on website entry again
            with open('Password container.txt', 'a') as writer:

                writer.write(text)
                site_entry.delete(0, END)
                password_entry.delete(0, END)
                site_entry.focus()

        else:
            # Show the user a messabox informing that the save has been cancelled
            messagebox.showinfo(title='Cancelled operation', message='The save operation has been succefully cancelled.')
            site_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

# Initialize the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Initialize and grid the canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Initialize and grid Website label & Website entry 
site_label = Label(text="Website:", pady=5)
site_label.grid(row=1, column=0)
site_entry = Entry(width=35)
site_entry.grid(row=1, column=1, columnspan=2, sticky='EW')
# Focus the text cursor in the site entry 
site_entry.focus()

# Initialize and grid email label & entry
user_label = Label(text="Email/Username:", pady=5)
user_label.grid(row=2, column=0)
user_entry = Entry(width=35)
user_entry.insert(0, "test@gmail.com")
user_entry.grid(row=2, column=1, columnspan=2, sticky='EW')

# Password label & entry
password_label = Label(text="Password:", pady=5)
password_label.grid(row=3, column=0)
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky='EW')

# Generate the password button
gen_button = Button(text="Generate Password", padx=10, command=generate_password)
gen_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Save", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()