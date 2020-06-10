import tkinter

root = tkinter.Tk()
root.title("Simple Calculator")


e = tkinter.Entry(root, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, sticky="nsew")


def button_click(number):
    e.insert("end", number)
def button_clear():
    e.delete(0, "end")
def button_add():
	global first_number
	first_number = e.get()
	e.delete(0, "end")
def button_calculate():
	answer = int(first_number) + int(e.get())
	e.delete(0, "end")
	e.insert(0, answer)

typHeight = 2
typWidth = 10
button_1 = tkinter.Button(root, text=("1"), height=typHeight, width=typWidth, command=lambda: button_click(1))
button_2 = tkinter.Button(root, text=("2"), height=typHeight, width=typWidth, command=lambda: button_click(2))
button_3 = tkinter.Button(root, text=("3"), height=typHeight, width=typWidth, command=lambda: button_click(3))
button_4 = tkinter.Button(root, text=("4"), height=typHeight, width=typWidth, command=lambda: button_click(4))
button_5 = tkinter.Button(root, text=("5"), height=typHeight, width=typWidth, command=lambda: button_click(5))
button_6 = tkinter.Button(root, text=("6"), height=typHeight, width=typWidth, command=lambda: button_click(6))
button_7 = tkinter.Button(root, text=("7"), height=typHeight, width=typWidth, command=lambda: button_click(7))
button_8 = tkinter.Button(root, text=("8"), height=typHeight, width=typWidth, command=lambda: button_click(8))
button_9 = tkinter.Button(root, text=("9"), height=typHeight, width=typWidth, command=lambda: button_click(9))
button_0 = tkinter.Button(root, text=("0"), height=typHeight, width=typWidth, command=lambda: button_click(0))
button_add = tkinter.Button(root, text=("+"), height=typHeight, width=typWidth, command=button_add)
button_equal = tkinter.Button(root, text=("="), command=button_calculate)
button_clear = tkinter.Button(root, text=("Clear"), command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2, sticky="nsew")
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2, sticky="nsew")
root.mainloop()
