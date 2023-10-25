from tkinter import *


def button_clicked():
    label.config(text=inputBox.get())


# def radio_used():
#     print(radio_state.get())
#
#
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
#
# def spinbox_used():
#     print(spinbox.get())
#
#
# def scale_used(value):
#     print(value)
#

# def checkbutton_used():
#     print(checked_state.get())
#

window = Tk()
window.title("My first GUI program")
window.config(padx=100, pady=200)
window.minsize(width=500, height=300)

label = Label(text="I am the label", font=("Inter", 15))
# label.pack()

label["text"] = "new text"
label.config(text="This is a new text")
# label.place(x=0, y=0)
label.grid(column=0, row=0)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

inputBox = Entry(width=30)
# inputBox.pack()
inputBox.grid(column=2, row=2)
#
inputBox.insert(END, string="Some text to begin with")
#
# text = Text(height=5, width=30)
# text.focus()
# text.insert(END, "Example of multi-line text entry.")
# # Gets current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checkbutton.pack()
#
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()
