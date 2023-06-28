from tkinter import *


def transform():
    miles_value = float(input.get())
    km_value = miles_value * 1.60934
    label.config(text="{:.2f}".format(km_value))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=50)
window.config(padx=35, pady=10)

miles = Label(text="miles")
miles.grid(row=0, column=2)

equal = Label(text= "is equal to")
equal.grid(row=1, column=0)

label = Label(text="0")
label.grid(row=1, column=1)

km = Label(text="Km")
km.grid(row=1, column=2)

input = Entry(width=10)
input.grid(row=0, column=1)

button = Button(text="Calculate", command=transform)
button.grid(row=2, column=1)

window.mainloop()