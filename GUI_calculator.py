import tkinter as tk # library used to make GUI application

calculation = "" # stores the current expression being built



def insert(symbol):
    
    global calculation # this function will use the calculation variable that was made earlier
    
    calculation += str(symbol) # converts the symbol that was pressed, into a string, and adds it to the calculation string
    
    result.delete("1.0", tk.END) # clears the current contents of the Text widget result. "1.0" is the starting position (line 1, char 0), and tk.END means "to the end"
    
    result.insert("1.0", calculation) # inserts the updated calculation string back into the Text widget, starting at line 1, character 0



def calculate(symbol=None):
    
    global calculation # this function will use the calculation variable that was made earlier
    
    try: # try-except block to handle potential evaluation errors
    
        calculation_result = str(eval(calculation))  # Evaluate safely and store result
    
        result.delete("1.0", tk.END)  # Clear the display
    
        result.insert("1.0", calculation_result)  # Show the result
    
        calculation = calculation_result

    except:
    
        result.delete("1.0", tk.END)  # Clear the display
    
        result.insert("1.0", "Error") # displays Error in the textbox
    
        calculation = "" # resets the string



def clear():
    
    global calculation # this function will use the calculation variable that was made earlier
    
    calculation = "" # resets the string
    
    result.delete("1.0", tk.END)  # Clear the display



root = tk.Tk() # creates the main window

root.geometry("300x250") # sets the dimensions of the window

root.title("Calculator") # sets a title of the window

result = tk.Text(root, height=2, width=16, font=("Arial", 24)) # creates a multi-line Text widget for displaying input/output, with height 2 lines, width 16 characters, and font size 24 in Arial

result.grid(columnspan=5) # places the Text widget in the grid layout and spans it across 5 columns



buttonframe = tk.Frame(root) # creates a container frame to hold all the buttons and attaches it to root
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

buttonframe.grid(row=1, column=0, columnspan=5, sticky="news") # places buttonframe into the main window's grid, on row 1, spanning 5 columns. sticky="news" makes it expand in all directions

for i in range(5):
    buttonframe.rowconfigure(i, weight=1)
for j in range(4):
    buttonframe.columnconfigure(j, weight=1)

root.rowconfigure(0, weight=1)  # result display

root.rowconfigure(1, weight=3)  # buttons

root.columnconfigure(0, weight=1)

btn1 = tk.Button(buttonframe, text="1", command=lambda: insert("1"))
btn1.grid(row=0, column=0, sticky="news")

btn2 = tk.Button(buttonframe, text="2", command=lambda: insert("2"))
btn2.grid(row=0, column=1, sticky="news")

btn3 = tk.Button(buttonframe, text="3", command=lambda: insert("3"))
btn3.grid(row=0, column=2, sticky="news")

btna = tk.Button(buttonframe, text="+", command=lambda: insert("+")) # addition
btna.grid(row=0, column=3, sticky="news")

btn4 = tk.Button(buttonframe, text="4", command=lambda: insert("4"))
btn4.grid(row=1, column=0, sticky="news")

btn5 = tk.Button(buttonframe, text="5", command=lambda: insert("5"))
btn5.grid(row=1, column=1, sticky="news")

btn6 = tk.Button(buttonframe, text="6", command=lambda: insert("6"))
btn6.grid(row=1, column=2, sticky="news")

btnsub = tk.Button(buttonframe, text="-", command=lambda: insert("-")) # subtraction
btnsub.grid(row=1, column=3, sticky="news")

btn7 = tk.Button(buttonframe, text="7", command=lambda: insert("7"))
btn7.grid(row=2, column=0, sticky="news")

btn8 = tk.Button(buttonframe, text="8", command=lambda: insert("8"))
btn8.grid(row=2, column=1, sticky="news")

btn9 = tk.Button(buttonframe, text="9", command=lambda: insert("9"))
btn9.grid(row=2, column=2, sticky="news")

btn0 = tk.Button(buttonframe, text="0", command=lambda: insert("0"))
btn0.grid(row=3, column=1, sticky="news")

btndot = tk.Button(buttonframe, text=".", command=lambda: insert("."))
btndot.grid(row=3, column=2, sticky="news")

btnmul = tk.Button(buttonframe, text="x", command=lambda: insert("*")) # multiplication
btnmul.grid(row=2, column=3, sticky="news")

clrbtn = tk.Button(buttonframe, text="C", command=clear) # clear function
clrbtn.grid(row=3, column=0, sticky="news")

btndiv = tk.Button(buttonframe, text="/", command=lambda: insert("/")) # division
btndiv.grid(row=3, column=3, sticky="news")

btnequal = tk.Button(buttonframe, text="=", command=calculate) # division
btnequal.grid(row=4, column=3, sticky="news")

root.mainloop() # starts the Tkinter event loop. Keeps the GUI running, listening for button clicks and user interaction