import customtkinter as ctk

root = ctk.CTk() # creates the main window

root.title("Unit Converter") # sets a title of the window

root.geometry("500x500") # sets the dimensions of the window

value_var = ctk.StringVar(master=root) # variable to hold the input value
unit_var = ctk.StringVar(master=root, value="meters")

def convert():
    pass

unit = ctk.CTkOptionMenu(
    root, variable=unit_var, values=["CentiMeters","Meters", "Kilometres"]
    )
unit.pack(pady=5, padx=5)

unit2 = ctk.CTkOptionMenu(
    root, variable=unit_var, values=["CentiMeters","Meters", "Kilometres"]
    )
unit2.pack(pady=5, padx=5)


label = ctk.CTkLabel(root, text="Enter number according the the unit selected.")
label.pack(pady=9, padx=5)

entry = ctk.CTkEntry(root, textvariable=value_var) # creates an entry widget
entry.pack(pady=10, padx=5)

convertbutton = ctk.CTkButton(root, text="convert", command=convert)
convertbutton.pack(padx=10, pady=10)

root.mainloop()