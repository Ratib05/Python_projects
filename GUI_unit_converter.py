import customtkinter as ctk

root = ctk.CTk() # creates the main window

root.title("Unit Converter") # sets a title of the window

root.geometry("300x250") # sets the dimensions of the window

value_var = ctk.StringVar() # variable to hold the input value

entry = ctk.Entry(root, textvariable=value_var) # creates an entry widget

root.mainloop()