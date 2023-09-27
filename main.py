import tkinter as tk
from tkinter import messagebox

EMAIL = "your@address.com"
ACTIVE_BUTTON = "#9bdeac"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = website_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \n"
                                               f"Email: {username}\nPassword: {password}\n"
                                               f"Is it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as f:
                f.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


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
website_entry = tk.Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = tk.Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, EMAIL)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)
password_button = tk.Button(text="Generate Password", activebackground=ACTIVE_BUTTON)
password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=44, command=save_data, activebackground=ACTIVE_BUTTON)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
