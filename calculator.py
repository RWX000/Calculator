from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("392x600")
window.resizable(0, 0)
window.configure(bg="sky blue")
Display = Entry(window,font='Arial 20',bd=20,bg="powder blue",width=22,justify="right",insertwidth=4).place(x=10,y=50)
  
  
button0=Button(window,text="0",width=4,height=3).place(x=17,y=180)
button1=Button(window,text="1",width=4,height=3).place(x=100,y=180)
button2=Button(window,text="2",width=4,height=3).place(x=183,y=180)
button3=Button(window,text="3",width=4,height=3).place(x=266,y=180)
button4=Button(window,text="4",width=4,height=3).place(x=17,y=255)
button5=Button(window,text="5",width=4,height=3).place(x=100,y=255)
button6=Button(window,text="6",width=4,height=3).place(x=183,y=255)
button7=Button(window,text="7",width=4,height=3).place(x=266,y=255)
button8=Button(window,text="8",width=4,height=3).place(x=17,y=330)
button9=Button(window,text="9",width=4,height=3).place(x=100,y=330)
button_c=Button(window,text="C",width=4,height=3).place(x=183,y=330)
button_equal=Button(window,text="=",width=4,height=3).place(x=266,y=330)
button_plus=Button(window,text="+",width=4,height=3).place(x=17,y=405)
button_minus=Button(window,text="-",width=4,height=3).place(x=100,y=405)
button_multiply=Button(window,text="*",width=4,height=3).place(x=183,y=405)
button_divide=Button(window,text="/",width=4,height=3).place(x=266,y=405)


window.mainloop()