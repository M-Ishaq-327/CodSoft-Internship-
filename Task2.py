import tkinter as tk
from tkinter import ttk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to perform arithmetic operations
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Stylish Calculator")

# Set a stylish theme
style = ttk.Style()
style.theme_use('clam')

# Entry field for input
entry = tk.Entry(root, font=("Helvetica", 24))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+', 'C'
]

# Create and place buttons
row_val = 1
col_val = 0

for label in button_labels:
    if label == 'C':
        ttk.Button(root, text=label, style='Calculator.TButton', command=clear).grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=10, ipady=10)
    else:
        ttk.Button(root, text=label, style='Calculator.TButton', command=lambda label=label: button_click(label) if label != '=' else calculate()).grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=10, ipady=10)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure button style
style.configure('Calculator.TButton', font=("Helvetica", 18))

# Run the GUI main loop
root.mainloop()
