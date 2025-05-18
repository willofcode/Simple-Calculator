# William Ng
# Simple calculator project

import tkinter as tk # GUI library
from tkinter import messagebox # for error messages

#  Arithmetic operation functions 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

#  Calculator state 
current_op = None
first_number = None
reset_next = False

#  Callback functions 
def on_digit(d):
    global reset_next # Reset the entry if needed
    if reset_next:
        entry.delete(0, tk.END)
        reset_next = False
    entry.insert(tk.END, str(d))


def on_decimal():
    global reset_next # Reset the entry if needed
    text = entry.get()
    if reset_next:
        entry.delete(0, tk.END)
    if "." not in text:
        entry.insert(tk.END, '.')
    reset_next = False


def on_toggle_sign():
    """Toggle the sign of the current entry number."""
    text = entry.get()
    if not text:
        return
    # Only toggle simple numeric values
    try:
        value = float(text)
        toggled = -value
        entry.delete(0, tk.END)
        # Remove .0 for integers
        if toggled.is_integer():
            entry.insert(tk.END, str(int(toggled)))
        else:
            entry.insert(tk.END, str(toggled))
    except ValueError:
        # Not a pure number; ignore
        pass


def on_operation(op):
    global current_op, first_number, reset_next
    try:
        first_number = float(entry.get())
        current_op = op
        reset_next = True
    except ValueError:
        messagebox.showerror("Error", "Invalid input.")
        entry.delete(0, tk.END)


def on_equals():
    global current_op, first_number, reset_next
    try:
        second_number = float(entry.get())
        if current_op == '+':
            result = add(first_number, second_number)
        elif current_op == '-':
            result = subtract(first_number, second_number)
        elif current_op == '*':
            result = multiply(first_number, second_number)
        elif current_op == '/':
            result = divide(first_number, second_number)
        else:
            messagebox.showerror("Error", "No operation selected.")
            return
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        current_op = None
        reset_next = True
    except Exception as e:
        messagebox.showerror("Error", str(e))


def on_clear():
    global current_op, first_number, reset_next
    entry.delete(0, tk.END)
    current_op = None
    first_number = None
    reset_next = False


def on_check_sign():
    try:
        value = float(entry.get())
        if value > 0:
            msg = "The number is positive."
        elif value < 0:
            msg = "The number is negative."
        else:
            msg = "The number is zero."
        messagebox.showinfo("Number Check", msg)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number to check.")

#  Build the GUI 
root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(
    root,
    width=16,
    font=('Arial', 24),
    bd=4,
    relief=tk.RIDGE,
    justify='right'
)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Button layout
buttons = [
    ('7', on_digit), ('8', on_digit), ('9', on_digit), ('/', on_operation),
    ('4', on_digit), ('5', on_digit), ('6', on_digit), ('*', on_operation),
    ('1', on_digit), ('2', on_digit), ('3', on_digit), ('-', on_operation),
    ('0', on_digit), ('.', on_decimal), ('=', on_equals), ('+', on_operation)
]

row = 1
col = 0
for (text, func) in buttons:
    if func in (on_digit, on_operation):
        action = lambda x=text, f=func: f(x)
    else:
        action = func
    tk.Button(
        root,
        text=text,
        width=4,
        height=2,
        font=('Arial', 18),
        command=action
    ).grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(
    root,
    text='C',
    width=4,
    height=2,
    font=('Arial', 18),
    command=on_clear
).grid(row=5, column=0, padx=2, pady=2)

# Toggle sign button
tk.Button(
    root,
    text='+/-',
    width=4,
    height=2,
    font=('Arial', 18),
    command=on_toggle_sign
).grid(row=5, column=1, padx=2, pady=2)

# Number checker button
tk.Button(
    root,
    text='Check Sign',
    width=10,
    height=2,
    font=('Arial', 18),
    command=on_check_sign
).grid(row=5, column=2, columnspan=2, padx=2, pady=2)

root.mainloop() # Start the GUI event loop

# This code is a simple calculator that supports basic arithmetic operations, toggling the sign of numbers, and checking if a number is positive, negative, or zero. It uses the tkinter library for the GUI and handles errors gracefully with message boxes.
# The calculator allows users to perform operations using buttons and displays results in a text entry field. It also includes a clear button to reset the calculator state.
# The calculator is designed to be user-friendly and provides feedback for invalid inputs.
# The code is structured to separate the GUI components from the logic, making it easier to maintain and extend in the future.