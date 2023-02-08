from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Initialize the window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Initialize the canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

site_label = Label(text="Website:")
site_label.grid(row=1, column=0)
site_entry = Entry(width=35)
site_entry.grid(row=1, column=1, columnspan=2)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

gen_button = Button(text="Generate Password")
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()