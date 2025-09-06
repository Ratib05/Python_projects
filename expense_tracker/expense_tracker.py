import customtkinter as ctk

root = ctk.CTk()

root.title("Expense tracker")

root.geometry("500x500")

def add_expense():
    pass

def del_expense():
    pass

title = ctk.CTkLabel(root, text="Simple expense tracker", font=ctk.CTk(size=18, weight="bold"))
title.grid(row=0, sticky="ew")

add = ctk.CTkButton(root, text="Add expense", command=add_expense)
add.grid(row=1, column=0, sticky="ew")

manage = ctk.CTkButton(root, text="manage categories", command=add_expense)
manage.grid(row=1, column=1, sticky="ew")

today = ctk.CTkLabel(root, text="")
today.grid(row=2, column=0, sticky="ew")

this_week = ctk.CTkLabel(root, text="")
this_week.grid(row=2, column=1, sticky="ew")

month = ctk.CTkLabel(root, text="")
month.grid(row=2, column=3, sticky="ew")

subtitle = ctk.CTkLabel(root, text="Expenses list")
subtitle.grid(row=3, column=0)

expenses_list = ctk.CTkFrame(root, bg_color="blue")
expenses_list.pack(row=4)



expense_date = ctk.CTkLabel(expenses_list, text="Date")
expense_date.grid(row=0, column=0)

expense_category = ctk.CTkLabel(expenses_list, text="Category")
expense_category.grid(row=0, column=1)

expense_amount = ctk.CTkLabel(expenses_list, text="Amount")
expense_amount.grid(row=0, column=2)

expense_note = ctk.CTkLabel(expenses_list, text="Note")
expense_note.grid(row=0, column=3)




root.mainloop()