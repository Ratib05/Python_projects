import random as r

import customtkinter as ctk

# Create the main application window
root = ctk.CTk()

# Set the window title
root.title("Password generator")

# Set the window size (width x height in pixels)
root.geometry("500x500")

# Set the background color of the main window
root.configure(fg_color="grey")  # Change this to your desired color

def on_click():
    pass

label = ctk.CTkLabel(root, text="Press button to generate password", font=("Arial", 16, "bold"), text_color="black")
label.grid(row=0, column=1)

button = ctk.CTkButton(root, text="Click Me", command=on_click, fg_color="blue")
button.grid(row=1, column=1)

root.mainloop()