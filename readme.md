# Simple Calculator

This repository contains two implementations of a simple calculator in Python:

1. **Terminal-Based Calculator** (`terminal-calculator.py`)
2. **GUI-Based Calculator** (`calculator.py`)

Both versions support: addition, subtraction, multiplication, division (with zero-check), toggling the sign of the current value, and checking whether the current value is positive, negative, or zero.

---

## Prerequisites

* **Python 3.x** installed on your system.
* For the GUI version, the **tkinter** library (usually included with most Python installations). On some Linux distributions, you may need to install it manually:

  ```bash
  sudo apt update
  sudo apt install python3-tk
  ```

---

## 1. Terminal-Based Calculator

### Files

* `terminal-calculator.py`: A REPL-style calculator that runs in your terminal.

### Usage

1. Open a terminal and navigate to the directory containing `terminal-calculator.py`.
2. Run:

   ```bash
   python3 terminal-calculator.py
   ```
3. Follow on-screen prompts:

   * **Initial value**: enter an integer or float to begin.
   * **Commands**:

     * `+`, `-`, `*`, `/`: apply an operation to the current value
     * `t`: toggle the sign of the current value
     * `c`: check if the current value is positive, negative, or zero
     * `clear`: reset current value to 0
     * `exit`: quit the calculator

Example session:

```
Enter initial value: 5
Current value: 5.0
Enter command (+, -, *, /, t, c, clear, exit): +
Enter next value: 3
Result: 8.0
Enter command: t
Result: -8.0
Enter command: c
The number is negative.
Enter command: exit
Exiting. Goodbye!
```

---

## 2. GUI-Based Calculator

### Files

* `calculator.py`: A Tkinter‑based graphical calculator window.

### Usage

1. Ensure you have `tkinter` installed.
2. Open a terminal and navigate to the directory containing `calculator.py`.
3. Run:

   ```bash
   python3 calculator.py
   ```
4. A window titled **Simple Calculator** will appear with:

   * A numeric display
   * Buttons for digits `0–9`, `.` (decimal), `+`, `-`, `*`, `/`, `=`
   * `C` to clear the display
   * `+/-` to toggle the current entry’s sign
   * `Check Sign` to pop up whether the current entry is positive, negative, or zero

---

## Code Structure

* **Terminal Version** is implemented procedurally with a `Calculator` class encapsulating state and command methods.
* **GUI Version** follows an OOP approach in `CalculatorApp`, binding UI elements to handler methods.

---

## License

This project is released under the MIT License.
