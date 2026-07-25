from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def write():
    with open("passwords.txt","a") as file:
        website = website_entry.get()
        email_username = username_entry.get()
        password = password_entry.get()
        if len(password)==0 or len(email_username)==0 or len(password) ==0:
            messagebox.showerror(title="Error",message="One or more fields are empty. ")
        else:
            yes_or_no = messagebox.askokcancel(title=website,
                                               message=f"There are the details entered \n Website: {website} \n Email: {email_username} \n Password: {password} \n is it ok or not?  ")
            if yes_or_no:
                file.write(f"{website}   ||   {email_username}    ||   {password} \n")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70,pady=60)

# Make columns 1 and 2 behave consistently for spanning widgets
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=180)

canvas.create_image(100,90,image=photo)
canvas.grid(row=0,column=1,columnspan=2)

label_website=Label(text="Website: ")
label_website.grid(row=1,column=0,sticky="E",pady=5)
label_username=Label(text="email/username: ")
label_username.grid(row=2,column=0,sticky="E",pady=5)
label_password=Label(text="password: ")
label_password.grid(row=3,column=0,sticky="E",pady=5)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2,sticky="EW",pady=5)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2,column=1,columnspan=2,sticky="EW",pady=5)
username_entry.insert(0,"samad57@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1,sticky="EW",pady=5)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2,sticky="EW",pady=5)

add_button = Button(text="ADD",width=36,command=write)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW",pady=5)

window.mainloop()