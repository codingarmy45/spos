# Import the tkinter module for GUI creation
import tkinter as tk

# Function to handle button clicks
def on_button_click(value):
    # Get the current content of the entry widget
    current = entry.get()
    # Clear the entry widget
    entry.delete(0, tk.END)
    # Insert the concatenation of the current content and the clicked button value
    entry.insert(tk.END, str(current) + str(value))

# Function to clear the entry widget
def clear_entry():
    # Delete the content of the entry widget
    entry.delete(0, tk.END)

# Function to evaluate and display the result
def calculate_result():
    try:
        # Evaluate the expression entered in the entry widget
        result = eval(entry.get())
        # Clear the entry widget
        entry.delete(0, tk.END)
        # Display the result in the entry widget
        entry.insert(tk.END, str(result))
    except Exception as e:
        # Handle exceptions (e.g., division by zero) by displaying an error message
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
# Set the title of the window
root.title("Calculator")

# Create an entry widget for displaying and entering values
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the labels for calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Initialize row and column values for grid placement
row_val = 1
col_val = 0

# Create and place buttons in a grid
for button in buttons:
    # Use lambda to pass the button value to the click function
    tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: on_button_click(b) if b != '=' else calculate_result()).grid(row=row_val, column=col_val)
    
    # Increment column value, reset to 0 and increment row value if column exceeds 3
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button that spans two columns
tk.Button(root, text="Clear", padx=20, pady=20, command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)

# Run the main loop to display the GUI
root.mainloop()
