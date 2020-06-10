import tkinter

root = tkinter.Tk()
root.title("Simple Calculator")
first_number=None
operator=None


e = tkinter.Entry(root, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, sticky="nsew")


def button_click(number):
    e.insert("end", number)
def button_clear():
    e.delete(0, "end")
def button_add():
	global first_number,operator
	first_number = e.get()
	operator="+"
	e.delete(0, "end")
def button_subtract():
	global first_number,operator
	first_number = e.get()
	operator="-"
	e.delete(0, "end")
def button_multiply():
	global first_number,operator
	first_number = e.get()
	operator="*"
	e.delete(0, "end")
def button_divide():
	global first_number,operator
	first_number = e.get()
	operator="/"
	e.delete(0, "end")
def button_calculate(first_number,operator):
    second_number=e.get()
    if operator == "+":
        answer = int(first_number) + int(second_number)
        e.delete(0,"end")
        e.insert(0,answer)
    elif operator == "-":
        answer = int(first_number) - int(second_number)
        e.delete(0,"end")
        e.insert(0,answer)
    elif operator == "*":
        answer = int(first_number) * int(second_number)
        e.delete(0,"end")
        e.insert(0,answer)
    elif operator == "/":
        answer = int(first_number) / int(second_number)
        e.delete(0,"end")
        e.insert(0,answer)


typHeight = 3
typWidth = 7
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
button_subtract = tkinter.Button(root, text=("-"), height=typHeight, width=typWidth, command=button_subtract)
button_divide = tkinter.Button(root, text=("/"), height=typHeight, width=typWidth, command=button_divide)
button_multiply = tkinter.Button(root, text=("*"), height=typHeight, width=typWidth, command=button_multiply)
button_equal = tkinter.Button(root, text=("="), command=lambda: button_calculate(first_number, operator))
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
button_clear.grid(row=0, column=4, sticky="nsew")
button_add.grid(row=1, column=4)
button_subtract.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=4, column=4)
button_equal.grid(row=4, column=1, columnspan=2, sticky="nsew")
root.mainloop()
