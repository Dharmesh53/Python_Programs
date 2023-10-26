from tkinter import *
from fxns import *
from tkinter import messagebox
import pyperclip


def passmaker():
    key = generator()
    pyperclip.copy(key)
    pass_input.delete(0, END)
    pass_input.insert(0, key)


def add():
    if web_input.get() == "" or email_input.get() == "" or len(pass_input.get()) == 0:
        messagebox.showerror(title="Error", message="Incomplete data, Please fill all the fields !!")
    else:
        is_ok = messagebox.askokcancel(title="Final step", message=f"You have entered\n"
                                                                   f"Website : {web_input.get()}\n"
                                                                   f"Email :{email_input.get()}\n"
                                                                   f"Password: {pass_input.get()}\n"
                                                                   f"Do you want to save it ?\n")
        if is_ok:
            with open("data.txt", 'a') as data_file:
                data_file.write(f"{web_input.get()} || {email_input.get()} || {pass_input.get()} \n")
                web_input.delete(0, END)
                pass_input.delete(0, END)


window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=128, width=128)
logo = PhotoImage(file="lock.png")
canvas.create_image(64, 64, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

web_label = Label(text="Website  ", font=("Inter", 10))
web_input = Entry(width=35)
web_label.grid(column=0, row=1)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

email_label = Label(text="Email/Username  ", font=("Inter", 10))
email_input = Entry(width=35)
email_label.grid(column=0, row=2)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "dhiru7321r@gmail.com")

pass_label = Label(text="Password  ", font=("Inter", 10))
pass_input = Entry(width=21)
pass_label.grid(column=0, row=3)
pass_input.grid(column=1, row=3)

generate_button = Button(text="Generate", command=passmaker, width=14)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=add, width=35)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
