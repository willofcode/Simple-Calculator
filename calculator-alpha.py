# William Ng
# Simple calculator project version Alpha

import tkinter as tk # GUI library
from tkinter import messagebox # for error messages

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.current_op = None
        self.first_number = None
        self.reset_next = False
        self._build_gui()

    def _build_gui(self):
        # Entry display
        self.entry = tk.Entry(
            self.root,
            width=16,
            font=('Arial', 24),
            bd=4,
            relief=tk.RIDGE,
            justify='right'
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Digit and operator buttons
        button_map = [
            ('7', self.on_digit), ('8', self.on_digit), ('9', self.on_digit), ('/', self.on_operation),
            ('4', self.on_digit), ('5', self.on_digit), ('6', self.on_digit), ('*', self.on_operation),
            ('1', self.on_digit), ('2', self.on_digit), ('3', self.on_digit), ('-', self.on_operation),
            ('0', self.on_digit), ('.', self.on_decimal), ('=', self.on_equals), ('+', self.on_operation)
        ]
        row = 1
        col = 0
        for (text, cmd) in button_map:
            # Capture both text and cmd for lambda
            if cmd == self.on_digit or cmd == self.on_operation:
                action = (lambda x=text, f=cmd: f(x))
            else:
                action = cmd
            tk.Button(
                self.root,
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

        # Clear, toggle sign, and check sign buttons
        tk.Button(self.root, text='C', width=4, height=2,
                  font=('Arial', 18), command=self.on_clear).grid(row=5, column=0, padx=2, pady=2)
        tk.Button(self.root, text='+/-', width=4, height=2,
                  font=('Arial', 18), command=self.on_toggle_sign).grid(row=5, column=1, padx=2, pady=2)
        tk.Button(self.root, text='Check Sign', width=10, height=2,
                  font=('Arial', 18), command=self.on_check_sign).grid(row=5, column=2, columnspan=2, padx=2, pady=2)

    def on_digit(self, digit):
        if self.reset_next:
            self.entry.delete(0, tk.END)
            self.reset_next = False
        self.entry.insert(tk.END, digit)

    def on_decimal(self):
        text = self.entry.get()
        if self.reset_next:
            self.entry.delete(0, tk.END)
        if '.' not in text:
            self.entry.insert(tk.END, '.')
        self.reset_next = False

    def on_toggle_sign(self):
        text = self.entry.get().strip()
        if not text:
            return
        try:
            value = float(text)
            toggled = -value
            self.entry.delete(0, tk.END)
            formatted = str(int(toggled)) if toggled.is_integer() else str(toggled)
            self.entry.insert(tk.END, formatted)
        except ValueError:
            pass

    def on_operation(self, op):
        text = self.entry.get().strip()
        if not text:
            return
        try:
            self.first_number = float(text)
            self.current_op = op
            self.reset_next = True
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number before an operator.")
            self.entry.delete(0, tk.END)

    def on_equals(self):
        if self.current_op is None:
            messagebox.showerror("Error", "No operation selected.")
            return
        text = self.entry.get().strip()
        try:
            second = float(text) if text else 0.0
            if self.current_op == '+':
                result = self.first_number + second
            elif self.current_op == '-':
                result = self.first_number - second
            elif self.current_op == '*':
                result = self.first_number * second
            elif self.current_op == '/':
                if second == 0:
                    raise ValueError("Cannot divide by zero.")
                result = self.first_number / second
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            self.reset_next = True
            self.current_op = None
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def on_clear(self):
        self.entry.delete(0, tk.END)
        self.current_op = None
        self.first_number = None
        self.reset_next = False

    def on_check_sign(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showerror("Error", "Please enter a number to check.")
            return
        try:
            value = float(text)
            if value > 0:
                msg = "The number is positive."
            elif value < 0:
                msg = "The number is negative."
            else:
                msg = "The number is zero."
            messagebox.showinfo("Number Check", msg)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
