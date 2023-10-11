import json
import pyperclip
import string
import tkinter as tk
from random import randint, choice, shuffle
from tkinter import messagebox

EMAIL = "your@address.com"
ACTIVE_BUTTON = "#9bdeac"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = list(string.ascii_letters)
numbers = [str(n) for n in range(10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = random_letters + random_numbers + random_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pass():
    website = website_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Username: {data[website]['username']}\n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = tk.Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()
search_button = tk.Button(text="Search", width=14, activebackground=ACTIVE_BUTTON, command=search_pass)
search_button.grid(row=1, column=2)

username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = tk.Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, EMAIL)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)
password_button = tk.Button(text="Generate Password", activebackground=ACTIVE_BUTTON, command=password_generator)
password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=44, command=save_data, activebackground=ACTIVE_BUTTON)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
