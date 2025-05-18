# William Ng
# Simple terminal Calculator

class Calculator:
    """
    A simple terminal-based calculator supporting basic operations and sign checks.
    """
    def __init__(self):
        self.current = 0.0
        self.running = False
        self.commands = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            't': self.toggle_sign,
            'c': self.check_sign,
            'clear': self.reset,
            'exit': self.exit
        }

    #  Operation methods 
    def add(self, value):
        self.current += value
        self._print_current()

    def subtract(self, value):
        self.current -= value
        self._print_current()

    def multiply(self, value):
        self.current *= value
        self._print_current()

    def divide(self, value):
        if value == 0:
            print("Error: Cannot divide by zero.")
        else:
            self.current /= value
            self._print_current()

    def toggle_sign(self, _=None):
        """
        Toggle the sign of the current value.
        """
        self.current = -self.current
        self._print_current()

    def check_sign(self, _=None):
        """
        Print whether the current value is positive, negative, or zero.
        """
        if self.current > 0:
            print("The number is positive.")
        elif self.current < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")

    def reset(self, _=None):
        """Reset the current value to zero."""
        self.current = 0.0
        print(f"Current value reset to {self.current}")

    def exit(self, _=None):
        """Exit the calculator."""
        print("Exiting. Goodbye!")
        self.running = False

    #  Utility methods 
    def _print_current(self):
        print(f"Result: {self.current}")

    @staticmethod # Static method to avoid instance dependency
    def get_input(prompt):
        """
        Prompt the user and return an int or float based on input format.
        Repeats until valid numeric input is entered.
        """
        while True:
            s = input(prompt).strip()
            try:
                return int(s)
            except ValueError:
                try:
                    return float(s)
                except ValueError:
                    print("Invalid input. Please enter a numeric value (integer or float).")

    def run(self):
        print("Simple Terminal Calculator")
        self.current = self.get_input("Enter initial value: ")
        print(f"Current value: {self.current}")
        print("Commands:")
        print("  +, -, *, /  : operations")
        print("  t           : toggle sign")
        print("  c           : check if positive/negative/zero")
        print("  clear       : reset to 0")
        print("  exit        : quit")

        self.running = True
        while self.running:
            cmd = input("Enter command (+, -, *, /, t, c, clear, exit): ").strip().lower()
            action = self.commands.get(cmd)
            if action:
                if cmd in ('+', '-', '*', '/'):
                    value = self.get_input("Enter next value: ")
                    action(value)
                else:
                    action()
            else:
                print("Unknown command. Please try again.")

if __name__ == '__main__':
    Calculator().run()

# This code is a simple terminal-based calculator that supports basic arithmetic operations,
# sign toggling, and checking if the current value is positive, negative, or zero.
# It uses a command pattern to handle user input and operations, making it easy to extend
# with additional commands in the future. Following the principles of clean code and OOP,
# making it modular, easy to read and maintain.