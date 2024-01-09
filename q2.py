

from tkinter import * 
from currency_converter import Converter
from tkinter import messagebox

def Convert():
    x = list1.get(ACTIVE)
    y = list2.get(ACTIVE)

    try:
        amt = t1.get()
        amt = float(amt)
    except ValueError:
        messagebox.showinfo("Error","Please enter numberical value")

    if(x==y):
        l5.configure(text=str(amt))
    else:
        amount = Converter(x,y,amt)

    l5.configure(text=str(round(amount,2))+" "+y)
    
    t1.delete(0, END)



if(__name__ == '__main__'):
    wind = Tk()
    wind.title("Calculator")
    wind.config(bg="#FF9800")
    wind.geometry("500x420")

    From = IntVar()
    To = IntVar()

    f1 = Frame(wind, highlightthickness=2)

    f2 = Frame(wind, highlightthickness=2)

    l1 = Label(f2, text="Enter amount ")
    l2 = Label(f2, text="From ")
    l3 = Label(f2, text="To ")
    l4 = Label(f1, text="Converted amount: ")
    l5 = Label(f1)


    t1 = Entry(f2)
    
    list1 = Listbox(f2)
    list2 = Listbox(f2)

    btn3 = Button(wind, text="Convert", command=Convert)
   

    f1.pack(pady=10)
    l4.grid(row=4, column=1, padx=5)
    l5.grid(row=4, column=2)

    f2.pack()
    l1.grid(row=1, column=1, pady=5)
    t1.grid(row=1, column=2, pady=5)
    l2.grid(row=2, column=1, pady=5)
    l3.grid(row=2, column=2, pady=5)
    list1.grid(row=3, column=1, padx=10)
    list2.grid(row=3, column=2, padx=10)

    # btn1.pack(side="left",padx=130)
    btn3.pack(side="bottom")

    list1.insert(END,"INR")
    list1.insert(END,"USD")
    list1.insert(END,"EUR")
    list1.insert(END,"RUB")
    list1.insert(END,"JPY")

    list2.insert(END,"INR")
    list2.insert(END,"USD")
    list2.insert(END,"EUR")
    list2.insert(END,"RUB")
    list2.insert(END,"JPY")


    wind.mainloop()
