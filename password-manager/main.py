from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbol + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_input.delete(0,END)
    pass_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    web_info = web_input.get()
    email_info = email_input.get()
    pass_info = pass_input.get()
    data = f"{web_info} | {email_info} | {pass_info}\n"
    if len(web_info) == 0 or len(pass_info) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure dont left any of the field empty.")
    else:
        is_ok = messagebox.askokcancel(title=web_info, message=f"There are the details entered : \n"
        f"Email: {email_info}\nPassword: {pass_info}\nIs it okay to save ?")

        if is_ok:
            file = open("data.txt", "a")
            file.write(data)
            file.close()
            web_input.delete(0,END)
            pass_input.delete(0, END)
            web_input.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=190)
pass_image = PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=pass_image)
canvas.grid(column=1,row=0)

web_label = Label(text="Website:")
web_label.grid(column=0,row=1)
web_input = Entry(width=42)
web_input.grid(column=1,row=1, columnspan=2)
web_input.focus()
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
email_input = Entry(width=42)
email_input.grid(column=1,row=2, columnspan=2)
email_input.insert(0,"deveshgupta3740@gmail.com")
pass_label = Label(text="Password:")
pass_label.grid(column=0,row=3)
pass_input = Entry(width=24)
pass_input.grid(column=1,row=3)
pass_gen_button = Button(text="Generate Password", command=generate_password)
pass_gen_button.grid(column=2,row=3,sticky="W")
add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(column=1,row=4, columnspan=2)

window.mainloop()