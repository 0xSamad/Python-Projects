from tkinter import *

def calculate():
    number = float(miles_entry.get())
    number = number * 1.609
    number =  round(number,2)
    Km_value.config(text=f"{number} ")

window = Tk()
window.title("Miles To KM Converter")
window.config(padx=20,pady=20)

miles_entry = Entry(width=7)
miles_entry.insert(END, string="0")
miles_entry.grid(row=0, column=1, padx=15)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal = Label(text="is equal to")
is_equal.grid(row=1, column=0)

Km_value = Label(text="0")
Km_value.grid(row=1, column=1)

KM = Label(text="KM")
KM.grid(row=1, column=2)

button = Button(text="Calculate",command=calculate)
button.grid(row=2,column=1)

window.mainloop()