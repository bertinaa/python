from tkinter import *  # will import all the classes
from tkinter import messagebox  # this is just a piece of code (file) so we need to import it again
import random
import pyperclip
import json

FONT = ("Courier", 14, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password ="".join(password_list)
    pass_details.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file():
    website = site_name.get()
    username = user_details.get()
    password = pass_details.get()
    new_data = {
        website : {
        "username" : username,
        "password" : password,
    }
    }

    if website=="" or password=="":
        messagebox.showerror(title="Error",message="Please do not leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent = 4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
                #dumps new_data into file with 4 spaces between every word
                site_name.delete(0, END)
                pass_details.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# zeroth row
canvas = Canvas(width=200, height=190)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=pass_img)
canvas.grid(row=0, column=1)

# first row
website = Label()
website.config(text="Website: ", font=FONT)
website.grid(row=1, column=0)


site_name = Entry(width=35, borderwidth=0)
site_name.grid(row=1, column=1, columnspan=2, sticky="EW")
site_name.focus()  # this will make the mouse select/have focus in the website entry part
# second row
email = Label()
email.config(text="Email/Username: ", font=FONT)
email.grid(row=2, column=0)

user_details = Entry(width=35, borderwidth=0)
user_details.grid(row=2, column=1, columnspan=2, sticky="EW")
user_details.insert(0, "bertinaagnes@gmail.com")  # already fills up the email part for you starting from the 0th index

# third row
password = Label()
password.config(text="Password: ", font=FONT)
password.grid(row=3, column=0)

pass_details = Entry(width=28, borderwidth=0)
pass_details.grid(row=3, column=1, sticky="EW")

gen_pass = Button(text="Generate Password", borderwidth=0, bg="white", width=14,command=generate_password)
gen_pass.grid(row=3, column=2)

# fourth row
add = Button(text="Add", borderwidth=0, bg="white", width=45, command=write_to_file)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
