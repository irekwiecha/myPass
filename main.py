import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website = website_entry.get()

username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = tk.Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username = website_entry.get()

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)
password_button = tk.Button(text="Generate Password")
password_button.grid(row=3, column=2)
password = password_entry.get()

add_button = tk.Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
