from tkinter import *
FONT = ("Arial", 15, "normal")
FACTOR_CONV_MILES_TO_KM = 1.609


def button_clicked():
    take_input = float(entry.get())
    output = round(take_input * FACTOR_CONV_MILES_TO_KM)
    middle_label.config(text=output)


# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=50, pady=50)

# top_right_label 0, 2
top_right_label = Label(text="Miles", font=FONT)
top_right_label.grid(row=0, column=2)

# middle_left_label 1, 0
middle_left_label = Label(text="is equal to", font=FONT)
middle_left_label.grid(row=1, column=0)

# middle_label 1, 1
middle_label = Label(text=0, font=FONT)
middle_label.grid(row=1, column=1)

# middle_right_label 1, 2
middle_right_label = Label(text="Km", font=FONT)
middle_right_label.grid(row=1, column=2)

# button 2,1
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

# entry 0, 1
entry = Entry(width=10)
entry.grid(row=0, column=1)

window.mainloop()
