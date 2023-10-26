# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=60, pady=40)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=55)
website_input.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=55)
email_username_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=36)
password_input.grid(row=3, column=1,columnspan=1)

generate_password_button = Button(text="Generate Password",width=15)
generate_password_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add", width=47)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
