from tkinter import *
from tkinter import messagebox
import string
import numpy as np 
import pyperclip
import json

# ------------------------------------------------ SEARCH CREDENTIALS ------------------------------------------------ #

def search_credentials():
    
    """This function searches for existing 'website' stored in credentials data file. If the data file does not exist, 
    and error message is returned. If the website does not exist in the data file, a messagebox info is displayed. If 
    the website credentials exist they are displayed in a message box and the password is automatically copied into the 
    clipboard."""

    website = site_entry.get().lower()
    
    # CASE Data file exists
    try:
        with open('psw_data.json') as data_file:
            data = json.load(data_file)

    # CASE Data file does not exist
    except FileNotFoundError:
        messagebox.showerror(title='ERROR', message='No data File Found!')
        site_entry.focus()

    else:
        # CASE: Catch data if it's stored in file
        if website in data:
            
            selected_data_dict = data[website]  # This is the target dictionary with the data
            username = selected_data_dict['username']
            password = selected_data_dict['password']

            messagebox.showinfo(
                title='Credentials', 
                message=f'Credentials for {website}\n\nUsername: {username}\nPassword: {password}\n\nPassword copied in clipboard.')
            pyperclip.copy(password)

        # CASE Data is not stored in file
        else:
            messagebox.showinfo(title='Result not found', message=f"No details for the website '{website}' exists.")

# ------------------------------------------------ SAVE PASSWORD ------------------------------------------------ #

def save_password():

    """This function get the text in website, username and password entries and store them in a JSON file named 
    'psw_data.json'. If any of the entries is empty an error message is displayed and the user is not allowed to
    proceed. Furthermore, when the 'Save' button is clicked it appears a messagebox where the user can confirm the 
    choice or cancel it."""
    
    # Variables that contain entries text
    website = site_entry.get().lower()
    username = user_entry.get()
    psw  = password_entry.get()

    # CONTROL: If any of these fields is empty an error popup is displayed
    if website == '' or username == '' or psw == '':
        messagebox.showerror(title='Missing fields', message='You must fill all fields before proceeding!')

    # CONTROL: If all is correct it may continue
    else:

        # Set data to be stored in a JSON file
        data_to_json = {
            website: {
                "username": username, 
                "password": psw
            }
        }
      
        # Try to open (only if file already exists)
        try:
            with open('psw_data.json', 'r') as data_file:
                data = json.load(data_file) 
        
        # Write new data (In case file does not exist)
        except FileNotFoundError:
            with open('psw_data.json', 'w') as data_file:
                json.dump(data_to_json, data_file, indent=4)

        # Update data and warn the user in case of overwrite
        else:

            # CASE selected website already exists
            if website in data:
                
                # ASK if user wants to overwrite data
                is_ok = messagebox.askokcancel(
                    title='Warning', 
                    message=f"Data already exist for the website '{website}'\nDo you want to overwrite data?")

                # CASE User wants to overwrite 
                if is_ok:
                    data.update(data_to_json)
                    with open('psw_data.json', 'w') as data_file:
                        json.dump(data, data_file, indent=4)

                    site_entry.delete(0, END)
                    password_entry.delete(0, END)
                    site_entry.focus()

                # CASE User does NOT want to overwrite data
                else:
                    messagebox.showinfo(title='Deletd operation', message='Operation deleted successfully.')

            # CASE selected website is a new entry
            else:
                data.update(data_to_json)
                with open('psw_data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)

                site_entry.delete(0, END)
                password_entry.delete(0, END)
                site_entry.focus()

# ------------------------------------------------ PASSWORD GENERATOR ------------------------------------------------ #

def generate_password():
    
    """This function generate a random password composed by 4 lowercase letters, 4 uppercase letters, 
    2 numbers and 2 special characters. Also, thanks to pyperclip, the password is copied in clipboard."""

    # Delete the entry (for older passwords)
    password_entry.delete(0, END)

    # Create array of LOWERCASE letters and get 4 of them randomly 
    list_lower = np.array(list(string.ascii_lowercase))
    random_lower = np.random.choice(list_lower, size=4)

    # Create array of UPPERCASE letters and get 4 of them randomly
    list_upper = np.array(list(string.ascii_uppercase))
    random_upper = np.random.choice(list_upper, size=4)

    # Create array of NUMBERS and get 2 of them randomly
    list_number = np.arange(10)
    random_number = np.random.choice(list_number, size=2)

    # Create array of SPECIAL CHARACTERS and get 2 of them randomly
    spec_char = np.array(list("!@#$%&*()-_+={}[]\/^~<>?"))
    random_char = np.random.choice(spec_char, size=2)

    # Concatenate the arrays and shuffle them with a permutation
    concat_random = np.concatenate([random_char, random_number, random_lower, random_upper])
    concat_random_shuffled = concat_random[np.random.permutation(len(concat_random))]

    # Convert random shuffled array into a string and insert it into the password entry, also copy into the clipboard
    random_password = "".join(concat_random_shuffled)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ------------------------------------------------ UI SETUP ------------------------------------------------ #

###  ------------------------------------------------ Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

###  ------------------------------------------------ Canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

### ------------------------------------------------ Labels & Entries
### ---- Website label & entry 
site_label = Label(text="Website:", pady=5)
site_entry = Entry()

site_label.grid(row=1, column=0)
site_entry.grid(row=1, column=1, sticky='EW')

site_entry.focus()                                  

### ---- Username label & entry
user_label = Label(text="Email/Username:", pady=5)
user_entry = Entry(width=35)

user_label.grid(row=2, column=0)
user_entry.grid(row=2, column=1, columnspan=2, sticky='EW')

user_entry.insert(0, "emanueleimmesi@gmail.com")

### ---- Password label & entry
password_label = Label(text="Password:", pady=5)
password_entry = Entry()

password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, sticky='EW')

# ------------------------------------------------ Buttons 
### ----Button to generate a random password 
gen_button = Button(text="Generate Random Password", padx=10, command=generate_password)
gen_button.grid(row=3, column=2)

### ----Button to Save data 
add_button = Button(text="Save", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

### ----Button to search for existing credentials
search_button = Button(text="Search Credentials", command=search_credentials)
search_button.grid(row=1, column=2, sticky='EW')

window.mainloop()