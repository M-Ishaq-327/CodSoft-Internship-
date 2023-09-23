import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, f"{len(task_listbox.get(0, tk.END)) + 1}. {task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        update_task_numbers()

# Function to remove all tasks
def remove_all_tasks():
    task_listbox.delete(0, tk.END)

# Function to update task numbers
def update_task_numbers():
    tasks = task_listbox.get(0, tk.END)
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        task_listbox.insert(tk.END, task.replace(task.split(".")[0], str(i)))

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set the background color of the window
root.configure(bg="lightblue")

# Create a text entry widget for tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Create a button to add tasks with rounded edges and spacing
add_button = tk.Button(root, text="Add Task", command=add_task, bg="purple", fg="white", relief=tk.RAISED, borderwidth=2)
add_button.pack(pady=5)

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
task_listbox.pack()

# Create a button to remove selected tasks with rounded edges and spacing
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="red", fg="white", relief=tk.RAISED, borderwidth=2)
remove_button.pack(pady=5)

# Create a button to remove all tasks with rounded edges and spacing
remove_all_button = tk.Button(root, text="Remove All Tasks", command=remove_all_tasks, bg="red", fg="white", relief=tk.RAISED, borderwidth=2)
remove_all_button.pack(pady=5)

# Start the GUI application
root.mainloop()
