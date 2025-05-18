# William Ng
# Simple calculator project

import tkinter as tk
from tkinter import messagebox

# --- Task 1: Calculator operations ---
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

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation_var.get()
        if op == "Add":
            res = add(num1, num2)
        elif op == "Subtract":
            res = subtract(num1, num2)
        elif op == "Multiply":
            res = multiply(num1, num2)
        elif op == "Divide":
            res = divide(num1, num2)
        else:
            raise ValueError("Unknown operation.")
        label_result.config(text=f"Result: {res}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# --- Task 2: Positive/Negative/Zero checker ---
def check_number():
    try:
        n = float(entry_check.get())
        if n > 0:
            verdict = "positive"
        elif n < 0:
            verdict = "negative"
        else:
            verdict = "zero"
        label_check_result.config(text=f"The number is {verdict}.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# --- Build the GUI ---
root = tk.Tk()
root.title("Simple Calculator")

# Calculator frame
frame_calc = tk.LabelFrame(root, text="Calculator Operations", padx=10, pady=10)
frame_calc.pack(padx=10, pady=5, fill="x")

tk.Label(frame_calc, text="First Number:").grid(row=0, column=0, sticky="e")
entry_num1 = tk.Entry(frame_calc)
entry_num1.grid(row=0, column=1)

tk.Label(frame_calc, text="Second Number:").grid(row=1, column=0, sticky="e")
entry_num2 = tk.Entry(frame_calc)
entry_num2.grid(row=1, column=1)

tk.Label(frame_calc, text="Operation:").grid(row=2, column=0, sticky="e")
operation_var = tk.StringVar(value="Add")
tk.OptionMenu(frame_calc, operation_var, "Add", "Subtract", "Multiply", "Divide").grid(row=2, column=1)

tk.Button(frame_calc, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=5)
label_result = tk.Label(frame_calc, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2)

# Number checker frame
frame_check = tk.LabelFrame(root, text="Positive/Negative/Zero Checker", padx=10, pady=10)
frame_check.pack(padx=10, pady=5, fill="x")

tk.Label(frame_check, text="Enter a number:").grid(row=0, column=0, sticky="e")
entry_check = tk.Entry(frame_check)
entry_check.grid(row=0, column=1)

tk.Button(frame_check, text="Check", command=check_number).grid(row=1, column=0, columnspan=2, pady=5)
label_check_result = tk.Label(frame_check, text="")
label_check_result.grid(row=2, column=0, columnspan=2)

root.mainloop()
