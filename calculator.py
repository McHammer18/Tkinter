"""
Morgan Christensen

Simple calculator project to get used to tkinter
"""
from tkinter import *

# number storage
numbers = []


# functions
def add():
    numbers.append(e.get())
    global math
    math = "addition"
    # print(numbers)
    e.delete(0, END)


def subtract():
    numbers.append(e.get())
    global math
    math = "subtraction"
    # print(numbers)
    e.delete(0, END)


def multiply():
    numbers.append(e.get())
    global math
    math = "multiplication"
    # print(numbers)
    e.delete(0, END)


def divide():
    numbers.append(e.get())
    global math
    math = "division"
    # print(numbers)
    e.delete(0, END)


def entry(number):
    cur_num = e.get()
    e.delete(0, END)
    e.insert(0, str(cur_num) + str(number))


def equal():
    if math == "addition":
        numbers.append(e.get())
        # print(numbers)
        e.delete(0, END)
        answer = int(numbers[0]) + int(numbers[1])
        e.insert(0, str(answer))
        numbers.clear()
    elif math == "subtraction":
        numbers.append(e.get())
        # print(numbers)
        e.delete(0, END)
        answer = int(numbers[0]) - int(numbers[1])
        e.insert(0, str(answer))
        numbers.clear()
    elif math == "multiplication":
        numbers.append(e.get())
        # print(numbers)
        e.delete(0, END)
        answer = int(numbers[0]) * int(numbers[1])
        e.insert(0, str(answer))
        numbers.clear()
    elif math == "division":
        numbers.append(e.get())
        # print(numbers)
        e.delete(0, END)
        answer = int(numbers[0]) / int(numbers[1])
        e.insert(0, str(answer))
        numbers.clear()


def clear():
    numbers.clear()
    e.delete(0, END)


calc = Tk()
calc.title("Simple Calculator")

# Entry used as label for the numbers selected
e = Entry(calc, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Number Buttons
b1 = Button(calc, text="1", padx=40, pady=20, command=lambda: entry(1))
b2 = Button(calc, text="2", padx=40, pady=20, command=lambda: entry(2))
b3 = Button(calc, text="3", padx=40, pady=20, command=lambda: entry(3))
b4 = Button(calc, text="4", padx=40, pady=20, command=lambda: entry(4))
b5 = Button(calc, text="5", padx=40, pady=20, command=lambda: entry(5))
b6 = Button(calc, text="6", padx=40, pady=20, command=lambda: entry(6))
b7 = Button(calc, text="7", padx=40, pady=20, command=lambda: entry(7))
b8 = Button(calc, text="8", padx=40, pady=20, command=lambda: entry(8))
b9 = Button(calc, text="9", padx=40, pady=20, command=lambda: entry(9))
b0 = Button(calc, text="0", padx=40, pady=20, command=lambda: entry(0))

# Number buttons grid
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)

# Function Buttons
b_add = Button(calc, text="+", padx=39, pady=20, command=lambda: add())
b_subtract = Button(calc, text="-", padx=39, pady=20, command=lambda: subtract())
b_multiply = Button(calc, text="x", padx=39, pady=20, command=lambda: multiply())
b_divide = Button(calc, text="/", padx=39, pady=20, command=lambda: divide())
b_equal = Button(calc, text="=", padx=39, pady=20, command=lambda: equal())
b_clear = Button(calc, text="Clear", padx=135, pady=20, command=lambda: clear())


# Function button grid
b_add.grid(row=4, column=1)
b_subtract.grid(row=1, column=3)
b_multiply.grid(row=2, column=3)
b_divide.grid(row=3, column=3)
b_equal.grid(row=4, column=2)
b_clear.grid(row=5, columnspan=3, column=0)

calc.mainloop()
