import customtkinter as ctk

root = ctk.CTk() # creates the main window

root.title("Unit Converter") # sets a title of the window

root.geometry("500x500") # sets the dimensions of the window

value_var = ctk.StringVar(master=root) # variable to hold the input value
fromUnit = ctk.StringVar(master=root, value="Meters")
toUnit = ctk.StringVar(master=root, value="Meters")
result_var = ctk.StringVar(master=root, value="")   # NEW: will show result in the UI

def convert():
    try:
        result = 0
        x = float(value_var.get())
        u1 = fromUnit.get().lower()
        u2 = toUnit.get().lower()
        
        factors = {
            ("centiMeters", "meters"): 0.01,
            ("centiMeters", "kilometres"): 0.00001,
            ("meters", "centiMeters"): 100,
            ("meters", "kilometres"): 0.001,
            ("kilometres", "centiMeters"): 100000,
            ("kilometres", "meters"): 1000
        }

        if (u1, u2) in factors:
            result = x * factors[(u1, u2)]
            result_var.set(result)
        else:
            result_var.set("Invalid units")
    except:
        result_var.set("Enter a number")

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