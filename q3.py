
from tkinter import * 

from tkinter import messagebox
def add():
    try:
        num1=t1.get()
        num2=t2.get()
        sum=int(num1)+int(num2)
        t1.delete(0,END)
        t2.delete(0,END)
        t1.focus()
        l3.configure(text="ADDITION IS"+str(sum))
    except:
        messagebox.showerror("error","Enter valid numbers")
def sub():
    try:
        num1=t1.get()
        num2=t2.get()
        sum=int(num1)-int(num2)
        t1.delete(0,END)
        t2.delete(0,END)
        t1.focus()
        l3.configure(text="SUBTACION IS"+str(sum))
    except:
        messagebox.showerror("error","Enter valid numbers")
def mul():
    try:
        num1=t1.get()
        num2=t2.get()
        sum=int(num1)*int(num2)
        t1.delete(0,END)
        t2.delete(0,END)
        t1.focus()
        l3.configure(text="MULTIPLICATION IS"+str(sum))
    except:
        messagebox.showerror("error","Enter valid numbers")        
def div():
    try:
        num1=t1.get()
        num2=t2.get()
        sum=int(num1)/int(num2)
        t1.delete(0,END)
        t2.delete(0,END)
        t1.focus()
        l3.configure(text="DIVISION IS"+str(sum))
    except:
        messagebox.showerror("error","Enter valid numbers")

if(__name__ == '__main__'):
    window = Tk()
    window.title("BASIC CALCULATOR PROGRAM")
    window.config(bg="#F58670")
    window.geometry("500x420")


    l1 = Label(window, text="ENTER THE FIRST NUMBER:")
    
    l2 = Label(window, text="ENTER THE SECOND NUMBER:")
    
    l3 = Label(window)


    t1 = Entry()
    t2 = Entry()
    
    b1 = Button(window, text="ADDITION", command=add)
    b2 = Button(window, text="SUBTRACTION", command=sub)
    b3 = Button(window, text="MULTIPLICATION", command=mul)
    b4 = Button(window, text="DIVISION", command=div)
    l1.grid(row=0,column=0)
    l2.grid(row=1,column=0)
    l3.grid(row=2,column=1)
    t1.grid(row=0,column=1)
    t2.grid(row=1,column=1)
    b1.grid(row=3,column=0)
    b2.grid(row=3,column=1)
    b3.grid(row=3,column=2)
    b4.grid(row=3,column=3)
    window.mainloop()