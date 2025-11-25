# Import the customtkinter library for modern UI components
import customtkinter as ctk

# Create the main application window
root = ctk.CTk()

# Set the window title
root.title("Expense tracker")

# Set the window size (width x height in pixels)
root.geometry("500x500")

# Function to handle adding a new expense
# TODO: Implement logic to add expense to database/storage
def add_expense():
    pass

# Function to handle deleting an expense
# TODO: Implement logic to remove expense from database/storage
def del_expense():
    pass

# ===== HEADER SECTION =====
# Main title label with bold, larger font
title = ctk.CTkLabel(root, text="Simple expense tracker", font=ctk.CTkFont(size=18, weight="bold"))
title.grid(row=0, sticky="ew")  # Stretch horizontally across the window

# ===== BUTTON SECTION =====
# Button to add a new expense entry
add = ctk.CTkButton(root, text="Add expense", command=add_expense)
add.grid(row=1, column=0, sticky="ew")  # Place in row 1, column 0

# Button to manage expense categories (e.g., Food, Transport, etc.)
manage = ctk.CTkButton(root, text="manage categories", command=add_expense)
manage.grid(row=1, column=1, sticky="ew")  # Place in row 1, column 1

# ===== SUMMARY SECTION =====
# Label to display today's total expenses
# TODO: Calculate and display today's expenses
today = ctk.CTkLabel(root, text="")
today.grid(row=2, column=0, sticky="ew")

# Label to display this week's total expenses
# TODO: Calculate and display week's expenses
this_week = ctk.CTkLabel(root, text="")
this_week.grid(row=2, column=1, sticky="ew")

# Label to display this month's total expenses
# TODO: Calculate and display month's expenses
month = ctk.CTkLabel(root, text="")
month.grid(row=2, column=3, sticky="ew")

# ===== EXPENSES LIST SECTION =====
# Subtitle for the expenses list section
subtitle = ctk.CTkLabel(root, text="Expenses list")
subtitle.grid(row=3, column=0)

# Container frame for the expenses list with blue background
expenses_list = ctk.CTkFrame(root, fg_color="blue")
expenses_list.grid(row=4, column=0, columnspan=4, sticky="ew")  # Span across 4 columns

# ===== EXPENSES LIST HEADERS =====
# Header: Date column
expense_date = ctk.CTkLabel(expenses_list, text="Date")
expense_date.grid(row=0, column=0, padx=10, )

# Header: Category column (e.g., Food, Rent, etc.)
expense_category = ctk.CTkLabel(expenses_list, text="Category")
expense_category.grid(row=0, column=1, padx=10)

# Header: Amount column (expense value)
expense_amount = ctk.CTkLabel(expenses_list, text="Amount")
expense_amount.grid(row=0, column=2, padx=10)

# Header: Note column (optional description)
expense_note = ctk.CTkLabel(expenses_list, text="Note")
expense_note.grid(row=0, column=3, padx=10)

# TODO: Add scrollable frame to display actual expense entries below headers
# TODO: Implement data persistence (JSON, SQLite, or CSV)
# TODO: Add delete/edit functionality for individual expenses

# Start the application event loop
root.mainloop()