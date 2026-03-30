from tkinter import *

# creating the main window for the calculator, giving it a title, size and making it non-resizable
window = Tk()
window.title("Calculator")
window.geometry("400x500")
window.resizable(0, 0)

# Creating the display for the calculator end giving it a font, border, width and relief
Display = Entry(window,font='Arial 15',bd=5,width=30,relief=SUNKEN)
Display.grid(padx=20, pady=10)


Buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '='
]

Buttons=Button(window,text=Buttons,font='Arial 15',bd=5,width=30,relief=SUNKEN)
Buttons.grid(padx=20, pady=10)




window.mainloop()