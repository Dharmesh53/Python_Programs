from tkinter import *


def button_clicked():
    km = float(inputBox.get())
    value = km * 0.621371
    result_label.config(text=value)


window = Tk()
window.title("Kilometer to Miles Converter")
window.config(padx=50, pady=50)
window.minsize(width=380, height=200)

inputBox = Entry(width=8)
inputBox.grid(column=3, row=1)

km_label = Label(text="Kilometers", font=("Inter", 10))
km_label.grid(column=4, row=1)

is_equal_to_label = Label(text="is equal to", font=("Inter", 10))
is_equal_to_label.grid(column=2, row=2)
result_label = Label(text="0", font=("Inter", 10))
result_label.grid(column=3, row=2)
miles_label = Label(text="Miles", font=("Inter", 10))
miles_label.grid(column=4, row=2)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=3, row=3)

window.mainloop()
