from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    if password_input.get() != "":
        can_clear = messagebox.askyesno(title="Clear current input", message="Would you like to clear current "
                                                                             "password entered?")
        if can_clear:
            password_input.delete(0, END)
            password_input.insert(0,  password)
            pyperclip.copy(password)
    else:
        password_input.insert(0,  password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    if website == "" or email_username == "" or password == "":
        messagebox.showinfo(title="Invalid Information", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail/Username: {email_username} "
                                               f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email_username} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


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
website_input.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=55)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, "tsounguc@mail.gvsu.edu")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=36)
password_input.grid(row=3, column=1, columnspan=1)

generate_password_button = Button(text="Generate Password", width=15, command= generate_password)
generate_password_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add", width=47, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
