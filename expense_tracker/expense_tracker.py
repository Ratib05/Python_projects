# Import the customtkinter library for modern UI components
import customtkinter as ctk

# Create the main application window
root = ctk.CTk()

# Set the window title
root.title("Expense tracker")

# Set the window size (width x height in pixels)
root.geometry("500x500")

# Set the background color of the main window
root.configure(fg_color="grey")  # Change this to your desired color

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
title = ctk.CTkLabel(root, text="Simple expense tracker", font=ctk.CTkFont(size=18, weight="bold"), text_color="black")
title.grid(row=0, sticky="ew")  # Stretch horizontally across the window

# ===== BUTTON SECTION =====
# Button to add a new expense entry
add = ctk.CTkButton(root, text="Add expense", command=add_expense)
add.grid(row=1, column=0, sticky="ew", padx=10, pady=10)  # Place in row 1, column 0

# Button to manage expense categories (e.g., Food, Transport, etc.)
manage = ctk.CTkButton(root, text="manage categories", command=add_expense)
manage.grid(row=1, column=1, sticky="ew", padx=10, pady=10)  # Place in row 1, column 1

# ===== SUMMARY SECTION =====
# Label to display today's total expenses
# TODO: Calculate and display today's expenses
today = ctk.CTkLabel(root, text="Today $0.00", text_color="black")
today.grid(row=2, column=0, sticky="ew")

# Label to display this week's total expenses
# TODO: Calculate and display week's expenses
this_week = ctk.CTkLabel(root, text="This week $0.00", text_color="black")
this_week.grid(row=2, column=1, sticky="ew")

# Label to display this month's total expenses
# TODO: Calculate and display month's expenses
month = ctk.CTkLabel(root, text="This month $0.00", text_color="black")
month.grid(row=2, column=3, sticky="ew")

# ===== EXPENSES LIST SECTION =====
# Subtitle for the expenses list section
subtitle = ctk.CTkLabel(root, text="Expenses list", font=ctk.CTkFont(size=16, weight="bold"), text_color="black")
subtitle.grid(row=3, column=0)

# Container frame for the expenses list with blue background
expenses_list = ctk.CTkFrame(root, fg_color="white")
expenses_list.grid(row=4, column=0, columnspan=4, sticky="ew")  # Span across 4 columns

# ===== EXPENSES LIST HEADERS =====
# Header: Date column
expense_date = ctk.CTkLabel(expenses_list, text="Date", text_color="black")
expense_date.grid(row=0, column=0, padx=10, )

# Header: Category column (e.g., Food, Rent, etc.)
expense_category = ctk.CTkLabel(expenses_list, text="Category", text_color="black")
expense_category.grid(row=0, column=1, padx=10)

# Header: Amount column (expense value)
expense_amount = ctk.CTkLabel(expenses_list, text="Amount", text_color="black")
expense_amount.grid(row=0, column=2, padx=10)

# Header: Note column (optional description)
expense_note = ctk.CTkLabel(expenses_list, text="Note", text_color="black")
expense_note.grid(row=0, column=3, padx=10)

select = ctk.CTkLabel(root, text="Select", text_color="black")
select.grid(row=5, column=0, padx=10, pady=10)

# Start the application event loop
root.mainloop()