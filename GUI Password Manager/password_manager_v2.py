from tkinter import *
from tkinter import messagebox
import random
import json

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


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showerror(title="Error",message="No data file found. ")
    else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
            else:
                messagebox.showerror(title="Error", message=f"No details for {website} exist.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def write():
    website = website_entry.get()
    email_username = username_entry.get()
    password = password_entry.get()
    data = {
        website: {
            "email": email_username,
            "password": password
        }
    }
    if len(password) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="One or more fields are empty. ")
    else:
        yes_or_no = messagebox.askokcancel(title=website,
                                           message=f"There are the details entered \n Website: {website} \n Email: {email_username} \n Password: {password} \n is it ok or not?  ")
        if yes_or_no:
            try:
                with open("passwords.json","r") as file:
                    old_data = json.load(file)

            except :
                with open("passwords.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            else:
                old_data.update(data)
                with open("passwords.json","w") as write_file:
                    json.dump(old_data,write_file,indent=4)
            finally:
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

website_entry = Entry(width=32)
website_entry.grid(row=1,column=1,columnspan=2,sticky="W",pady=5)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2,column=1,columnspan=2,sticky="EW",pady=5)
username_entry.insert(0,"samad57@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1,sticky="EW",pady=5)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2,sticky="EW",pady=5,padx=5)

search_button = Button(text="Search",width=7,command=search_website)
search_button.grid(row=1,column=2,sticky="E")

add_button = Button(text="ADD",width=36,command=write)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW",pady=5)

window.mainloop()