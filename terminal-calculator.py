# William Ng
# Simple terminal Calculator

import sys

# --- Arithmetic operation functions ---
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


def toggle_sign(value):
    return -value


def check_sign(value):
    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"
    else:
        return "zero"


def get_input(prompt):
    """
    Prompt the user and return an int or float based on input format.
    Repeats until valid numeric input is entered.
    """
    while True:
        s = input(prompt).strip()
        try:
            # Try integer first
            return int(s)
        except ValueError:
            try:
                # Fallback to float
                return float(s)
            except ValueError:
                print("Invalid input. Please enter a numeric value (integer or float).")


def main():
    print("Simple Terminal Calculator")
    # Initial numeric value allowed
    current = get_input("Enter initial value: ")
    print(f"Current value: {current}")
    print("Commands:")
    print("  +, -, *, /  : operations")
    print("  t           : toggle sign of current value")
    print("  c           : check if current value is positive/negative/zero")
    print("  clear       : reset current value to 0")
    print("  exit        : quit the calculator")

    running = True
    while running:
        cmd = input("Enter command (+, -, *, /, t, c, clear, exit): ").strip().lower()
        if cmd == 'exit':
            print("Exiting. Goodbye!")
            running = False
        elif cmd == 'clear':
            current = 0
            print(f"Current value reset to {current}")
        elif cmd == 't':
            current = toggle_sign(current)
            print(f"Sign toggled. Current value: {current}")
        elif cmd == 'c':
            result = check_sign(current)
            print(f"The number is {result}.")
        elif cmd in ('+', '-', '*', '/'):
            num = get_input("Enter next value: ")
            try:
                if cmd == '+':
                    current = add(current, num)
                elif cmd == '-':
                    current = subtract(current, num)
                elif cmd == '*':
                    current = multiply(current, num)
                elif cmd == '/':
                    current = divide(current, num)
                print(f"Result: {current}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Unknown command. Please try again.")

    sys.exit(0)

if __name__ == '__main__':
    main()
