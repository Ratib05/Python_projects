import customtkinter as ctk

root = ctk.CTk() # creates the main window

root.title("Unit Converter") # sets a title of the window

root.geometry("500x500") # sets the dimensions of the window

value_var = ctk.StringVar(master=root) # variable to hold the input value
fromUnit = ctk.StringVar(master=root, value="Meters")
toUnit = ctk.StringVar(master=root, value="Meters")
result_var = ctk.StringVar(master=root, value="")   # NEW: will show result in the UI

def convert():
    result = 0
    x = float(value_var.get())
    u1 = fromUnit.get()
    u2 = toUnit.get()
    if u1 == "CentiMeters" and u2 == "Meters":
        result = x/100
        result_var.set(result)
    elif u1 == "CentiMeters" and u2 == "Kilometres":
        result = x/100000
        result_var.set(result)
    elif u1 == "Meters" and u2 == "CentiMeters":
        result = x*100
        result_var.set(result)
    elif u1 == "Meters" and u2 == "kilometres":
        result = x/1000
        result_var.set(result)
    elif u1 == "kilometres" and u2 == "CentiMeters":
        result = x*100000
        result_var.set(result)
    elif u1 == "kilometres" and u2 == "Meters":
        result = x/1000
        result_var.set(result)

unit = ctk.CTkOptionMenu(
    root, variable=fromUnit, values=["CentiMeters","Meters", "Kilometres"]
    )
unit.pack(pady=5, padx=5)

unit2 = ctk.CTkOptionMenu(
    root, variable=toUnit, values=["CentiMeters","Meters", "Kilometres"]
    )
unit2.pack(pady=5, padx=5)

label = ctk.CTkLabel(root, text="Enter number according the the unit selected.")
label.pack(pady=9, padx=5)

entry = ctk.CTkEntry(root, textvariable=value_var) # creates an entry widget
entry.pack(pady=10, padx=5)

convertbutton = ctk.CTkButton(root, text="convert", command=convert)
convertbutton.pack(padx=10, pady=10)

result_label = ctk.CTkLabel(root, textvariable=result_var, text=toUnit)
result_label.pack(pady=8)

root.mainloop()