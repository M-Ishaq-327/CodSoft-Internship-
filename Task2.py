import tkinter as tk

# Function to perform arithmetic operations
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()
    
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplycation":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            result_label.config(text="Cannot divide by zero")
            return
        result = num1 / num2
    else:
        result_label.config(text="Invalid operation")
        return
    
    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")  


label1 = tk.Label(root, text="Enter the first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter the second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

operation_var = tk.StringVar()
operation_var.set("Addition")  # Default selection
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_label = tk.Label(root, text="Select operation:")
operation_label.pack()

for operation in operations:
    radio_button = tk.Radiobutton(root, text=operation, variable=operation_var, value=operation)
    radio_button.pack()


calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()


result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
