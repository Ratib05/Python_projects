# Import the customtkinter library for modern UI components
import customtkinter as ctk
import datetime as dt
import sqlite3

# Create the main application window
root = ctk.CTk()

# Set the window title
root.title("Expense tracker")

# Set the window size (width x height in pixels)
root.geometry("500x500")

# Set the background color of the main window
root.configure(fg_color="grey")  # Change this to your desired color

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    note TEXT )"""
    )

conn.commit()

# Function to handle adding a new expense

expenses_schema = {
    "date": {"type": lambda s: s, "required": True},
    "category": {"type": str, "required": True},
    "amount": {"type": float, "required": True},
    "note": {"type": str, "required": False, "default": ""},
}
def add_expense():

    # DATE DIALOG BOX

    dialog1 = ctk.CTkToplevel(root)
    dialog1.title("Date")
    dialog1.geometry("300x150")

    date = ctk.CTkEntry(dialog1, placeholder_text= "YYYY-MM-DD")
    date.grid(row=1, column=1)

    root.wait_window(dialog1)

    value1 = date.get()

    ok_btn = ctk.CTkButton(dialog1, text="OK", command=lambda:dialog1.destroy())
    ok_btn.grid(row=2, column=1)

    # CATEGORY DIALOG BOX

    dialog2 = ctk.CTkToplevel(root)
    dialog2.title("Category")
    dialog2.geometry("300x150")
    
    var2 = ctk.StringVar()
    category = ctk.CTkOptionMenu(dialog2, values=["Food", "Entertainment", "Transport", "Bills"], variable=var2)
    category.grid(row=0, column=1)
    category.set("Food")

    root.wait_window(dialog2)

    value2 = category.get()

    ok_btn = ctk.CTkButton(dialog1, text="OK", command=lambda:dialog1.destroy())
    ok_btn.grid(row=2, column=1)

    # AMOUNT DIALOG BOX

    dialog3 = ctk.CTkToplevel(root)
    dialog3.title("Amount")
    dialog3.geometry("300x150")

    amount = ctk.CTkEntry(dialog3, placeholder_text= "Amount spent")
    amount.grid(row=0, column=1)

    root.wait_window(dialog3)

    value3 = amount.get()

    ok_btn = ctk.CTkButton(dialog3, text="OK", command=lambda:dialog3.destroy())
    ok_btn.grid(row=2, column=1)

    # NOTE DIALOG BOX

    dialog4 = ctk.CTkToplevel(root)
    dialog4.title("Note")
    dialog4.geometry("300x150")

    note = ctk.CTkEntry(dialog4, placeholder_text= "Additional details: ")
    note.grid(row=1, column=1)

    root.wait_window(dialog4)

    value4 = note.get()

    ok_btn = ctk.CTkButton(dialog4, text="OK", command=lambda:dialog4.destroy())
    ok_btn.grid(row=2, column=1)

    # ADD TO DATABASE LOGIC

    raw_data = {
        "date": value1,
        "category": value2,
        "amount": float(value3),
        "note": value4
    }

    cursor.execute(
        """ INSERT INTO expenses (date, category, amount, note) 
        VALUES (?, ?, ?, ?) """, 
        (raw_data["date"],
        raw_data["category"],
        raw_data["amount"],
        raw_data["note"])
    )

    conn.commit()
    print("Expense saved.")
    display_expenses()

# Function to handle deleting an expense
# TODO: Implement logic to remove expense from database/storage
def del_expense():
    pass

def select_expense():
    pass

def display_expenses():
    
    for widget in expenses_list.winfo_children():
        if widget.grid_info()["row"] > 0:
            widget.destroy()

    cursor.execute("SELECT date, category, amount, note FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()

    row_num = 1
    for date, category, amount, note in rows:
        ctk.CTkLabel(expenses_list, text=date, text_color="black").grid(row=row_num, column=0, padx=10, pady=5)
        ctk.CTkLabel(expenses_list, text=category, text_color="black").grid(row=row_num, column=1, padx=10, pady=5)
        ctk.CTkLabel(expenses_list, text=f"${amount:.2f}", text_color="black").grid(row=row_num, column=2, padx=10, pady=5)
        ctk.CTkLabel(expenses_list, text=note, text_color="black").grid(row=row_num, column=3, padx=10, pady=5)
        row_num += 1

# ===== HEADER SECTION =====
# Main title label with bold, larger font
title = ctk.CTkLabel(root, text="Simple expense tracker", font=ctk.CTkFont(size=18, weight="bold"), text_color="black")
title.grid(row=0, sticky="ew")  # Stretch horizontally across the window

summary_section = ctk.CTkFrame(root, fg_color="white")
summary_section.grid(row=2, column=0, columnspan=3, sticky="ew")

# ===== BUTTON SECTION =====
# Button to add a new expense entry
add = ctk.CTkButton(summary_section, text="Add expense", command=add_expense)
add.grid(row=1, column=0, sticky="ew", padx=10, pady=10)  # Place in row 1, column 0

# Button to manage expense categories (e.g., Food, Transport, etc.)
manage = ctk.CTkButton(summary_section, text="manage categories")
manage.grid(row=1, column=1, sticky="ew", padx=10, pady=10)  # Place in row 1, column 1

# ===== SUMMARY SECTION =====
# Label to display today's total expenses
# TODO: Calculate and display today's expenses
today = ctk.CTkLabel(summary_section, text="Today $0.00", text_color="black")
today.grid(row=2, column=0, sticky="ew")

# Label to display this week's total expenses
# TODO: Calculate and display week's expenses
this_week = ctk.CTkLabel(summary_section, text="This week $0.00", text_color="black")
this_week.grid(row=2, column=1, sticky="ew")

# Label to display this month's total expenses
# TODO: Calculate and display month's expenses
month = ctk.CTkLabel(summary_section, text="This month $0.00", text_color="black")
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
expense_date.grid(row=0, column=0, padx=10, stick="ew")

# Header: Category column (e.g., Food, Rent, etc.)
expense_category = ctk.CTkLabel(expenses_list, text="Category", text_color="black")
expense_category.grid(row=0, column=1, padx=10, stick="ew")

# Header: Amount column (expense value)
expense_amount = ctk.CTkLabel(expenses_list, text="Amount", text_color="black")
expense_amount.grid(row=0, column=2, padx=10, stick="ew")

# Header: Note column (optional description)
expense_note = ctk.CTkLabel(expenses_list, text="Note", text_color="black")
expense_note.grid(row=0, column=3, padx=10, stick="ew")

select = ctk.CTkButton(root, text="Select", text_color="black", command=select_expense)
select.grid(row=5, column=0, padx=10, pady=10)

delete = ctk.CTkButton(root, text="Delete", text_color="black", command=del_expense)
delete.grid(row=5, column=1, padx=10, pady=10)

graph_section = ctk.CTkFrame(root, fg_color="white")
graph_section.grid(row=6, columnspan=3)

# Start the application event loop
display_expenses()
root.mainloop()