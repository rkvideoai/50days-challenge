#Day 2/50 - AI Python Challenge
#Basic Calculator : Simple calculator for two numbers with +, -, *, / operations.

import tkinter as tk  # Importing the tkinter module for GUI

# Function to update the expression in the entry field
def press(key):
    current = entry_var.get()  # Get the current value in the input box
    entry_var.set(current + key)  # Add the pressed key to the input box

# Function to evaluate the expression and show the result
def calculate():
    try:
        expression = entry_var.get()  # Get the full expression from input box
        result = eval(expression)   # Calculate the result using eval()
        entry_var.set(result)       # Show the result in the input box
    except:
        entry_var.set("Error")      # If there's an error (like division by zero), show "Error"

# Function to clear the input box
def clear():
    entry_var.set("")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Variable to store the current expression
entry_var = tk.StringVar()

# Entry widget to show the expression/result
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, insertwidth=2,
                 width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons (layout of the calculator)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'  # Clear button
]

# Place buttons in the grid
row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
                  command=calculate, bg="orange").grid(row=row, column=col)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
                  command=clear, bg="lightgray").grid(row=5, column=0, columnspan=4, sticky="we")
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
                  command=lambda k=button: press(k)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI loop
root.mainloop()