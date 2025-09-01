import customtkinter as ctk
import tkinter as tk

root = ctk.CTk() # creates the main window

root.title("Unit Converter") # sets a title of the window

root.geometry("500x500") # sets the dimensions of the window

value_var = ctk.StringVar(master=root) # variable to hold the input value
fromUnit = ctk.StringVar(master=root, value="Meters")
toUnit = ctk.StringVar(master=root, value="Meters")
result_var = ctk.StringVar(master=root, value="")   # NEW: will show result in the UI
button_pressed = tk.BooleanVar(value=False)

def convert():
    try:
        result = 0
        button_pressed.set(True)
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

        #CHG: show Clear button after any convert attempt
        if not clear_btn.winfo_ismapped():
            clear_btn.grid(row=5, column=1, pady=5)
        
    except ValueError:                                   # CHG: specific exception
        result_var.set("Enter a number")
        if not clear_btn.winfo_ismapped():               # CHG: show even on error
            clear_btn.grid(row=5, column=1, pady=5)


def swap_units():
    left = fromUnit.get()
    right = toUnit.get()
    toUnit.set(left)
    fromUnit.set(right)
    convert()

unit = ctk.CTkOptionMenu(
    root, variable=fromUnit, values=["CentiMeters","Meters", "Kilometres"]
    )
unit.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

unit2 = ctk.CTkOptionMenu(
    root, variable=toUnit, values=["CentiMeters","Meters", "Kilometres"]
    )
unit2.grid(row=0, column=2, pady=5, padx=5, sticky="ew")

swap_btn = ctk.CTkButton(root, text="⇆ Swap", command=swap_units)
swap_btn.grid(row=0, column=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

label = ctk.CTkLabel(root, text="Enter number according the the unit selected.")
label.grid(row=1, column=1, pady=9, padx=5)

entry = ctk.CTkEntry(root, textvariable=value_var) # creates an entry widget
entry.grid(row=2, column=1, pady=10, padx=5, sticky="ew")

convertbutton = ctk.CTkButton(root, text="convert", command=convert)
convertbutton.grid(row=3, column=1, padx=10, pady=10)

result_label = ctk.CTkLabel(root, textvariable=result_var, text=toUnit, 
                            font=ctk.CTkFont(size=18, weight="bold"))
result_label.grid(row=4, column=1, pady=8)

clear_btn = ctk.CTkButton(root, text="clear", command=lambda: [result_var.set(""), clear_btn.grid_remove()])


if button_pressed == True:
    clear_btn.grid(row=5, column=1, pady=5)

root.mainloop()