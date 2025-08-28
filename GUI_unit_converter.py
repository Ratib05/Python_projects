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
            ("centimeters", "meters"): 0.01,
            ("centimeters", "kilometres"): 0.00001,
            ("meters", "centimeters"): 100,
            ("meters", "kilometres"): 0.001,
            ("kilometres", "centimeters"): 100000,
            ("kilometres", "meters"): 1000,
            ("meters", "meters"): 1,
            ("centimeters", "centimeters"): 1,
            ("kilometres", "kilometres"): 1
        }

        if (u1, u2) in factors:
            result = x * factors[(u1, u2)]
            result_var.set(f"{result:.6g} {toUnit.get()}")
        else:
            result_var.set("Invalid units")
    except:
        result_var.set("Enter a number")


def swap_units():
    fromUnit.set(toUnit.get())
    toUnit.set(fromUnit.get())

unit = ctk.CTkOptionMenu(
    root, variable=fromUnit, values=["CentiMeters","Meters", "Kilometres"]
    )
unit.grid(row=0, column=0, padx=5, pady=5)

unit2 = ctk.CTkOptionMenu(
    root, variable=toUnit, values=["CentiMeters","Meters", "Kilometres"]
    )
unit2.grid(row=0, column=2, pady=5, padx=5)

unit.grid_columnconfigure(0, weight=1)
unit.grid_columnconfigure(1, weight=1)

label = ctk.CTkLabel(root, text="Enter number according the the unit selected.")
label.grid(row=1, column=1, pady=9, padx=5)

entry = ctk.CTkEntry(root, textvariable=value_var) # creates an entry widget
entry.grid(row=2, column=1, pady=10, padx=5)

convertbutton = ctk.CTkButton(root, text="convert", command=convert)
convertbutton.grid(row=3, column=1, padx=10, pady=10)

result_label = ctk.CTkLabel(root, textvariable=result_var, text=toUnit, 
                            font=ctk.CTkFont(size=18, weight="bold"))
result_label.grid(row=4, column=1, pady=8)

root.mainloop()