#importing packages
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

#Initializing GUI window
window=tk.Tk()
window.title("Calculator")
frame=tk.Frame(master = window, bg="Pink", padx=2)
frame.pack()
entry=tk.Entry(master = frame, relief=SUNKEN, borderwidth=10,width=40)
entry.grid(row=0,column=0,columnspan=3,pady=2,ipady=5)

#function for inserting the number
def click(number):
    entry.insert(tk.END,number)

#function for getting the answer
def equal():
   try:
    inp = str(eval(entry.get()))
    entry.delete(0,tk.END)
    entry.insert(0,inp)
   except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

#fuction to clear the screen
def clear():
    entry.delete(0,tk.END)

#Creating Buttons for entering values(numbers).
button1=tk.Button(frame,text="1",padx=15,pady=5,width=6,command=lambda: click("1"))
button1.grid(row=1,column=0,pady=3)
button2=tk.Button(frame,text="2",padx=15,pady=5,width=6,command=lambda: click("2"))
button2.grid(row=1,column=1,pady=3)
button3=tk.Button(frame,text="3",padx=15,pady=5,width=6,command=lambda: click("3"))
button3.grid(row=1,column=2,pady=3)
button4=tk.Button(frame,text="4",padx=15,pady=5,width=6,command=lambda: click("4"))
button4.grid(row=2,column=0,pady=3)
button5=tk.Button(frame,text="5",padx=15,pady=5,width=6,command=lambda: click("5"))
button5.grid(row=2,column=1,pady=3)
button6=tk.Button(frame,text="6",padx=15,pady=5,width=6,command=lambda: click("6"))
button6.grid(row=2,column=2,pady=3)
button7=tk.Button(frame,text="7",padx=15,pady=5,width=6,command=lambda: click("7"))
button7.grid(row=3,column=0,pady=3)
button8=tk.Button(frame,text="8",padx=15,pady=5,width=6,command=lambda: click("8"))
button8.grid(row=3,column=1,pady=3)
button9=tk.Button(frame,text="9",padx=15,pady=5,width=6,command=lambda: click("9"))
button9.grid(row=3,column=2,pady=3)
button0=tk.Button(frame,text="0",padx=15,pady=5,width=6,command=lambda: click("0"))
button0.grid(row=4,column=1,pady=3)

#Creating buttons for Arithmetic operations.
button_add=tk.Button(frame,text="+",padx=15,pady=5,width=6,command=lambda: click("+"))
button_add.grid(row=5,column=0,pady=3)
button_sub=tk.Button(frame,text="-",padx=15,pady=5,width=6,command=lambda: click("-"))
button_sub.grid(row=5,column=1,pady=3)
button_mul=tk.Button(frame,text="x",padx=15,pady=5,width=6,command=lambda: click("*"))
button_mul.grid(row=5,column=2,pady=3)
button_div=tk.Button(frame,text="/",padx=15,pady=5,width=6,command=lambda: click("/"))
button_div.grid(row=6,column=0,pady=3)

#Creating Buttons for equal and Clear for calculator
button_equal=tk.Button(frame,text="=",padx=15,pady=5,width=18,bg="Azure",command=lambda: equal())
button_equal.grid(row=7,column=0,columnspan=2,pady=3)
button_clear=tk.Button(frame,text="Clear",padx=15,pady=5,width=18,command=lambda: clear())
button_clear.grid(row=6,column=1,columnspan=2,pady=3)

window.update()
window.mainloop()
