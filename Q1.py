
data={}
def login():
    uname=t1.get()
    passw=t2.get()
    if len(uname)==0 or len(passw)==0:
        messagebox.showerror("error","USERNAME AND PASSWORD SHOULD NOT BE EMPTY" )
    else:
        for x,y in data.items():
            if uname==x and passw==y:
                messagebox.showinfo("success","login succesful")
                break
            else:
                messagebox.showinfo("login fail","invalid username and password")
def signup():
    uname=t1.get()
    passw=t2.get()
    if len(uname)==0 or len(passw)==0:
        messagebox.showerror("error","USERNAME AND PASSWORD SHOULD NOT BE EMPTY" )
    else:
        data[uname]=passw
        messagebox.showinfo("success","signup succesful")
if __name__=="__main__":
    window=Tk()
    window.configure(bg="#F6D776")
 
    window.title("LOGIN PAGE")
    window.geometry("400x400")
    l1=Label(window,text="ENTER USERNAME:")
    l2=Label(window,text="ENTER PASSWORD:")
    t1=Entry(window)
    t2=Entry(window,show="*")
    b1=Button(window,text="Log IN",command=login)
    b2=Button(window,text="Sign IN",command=signup)
    l1.grid(row=1,column=1)
    t1.grid(row=1,column=2)
    l2.grid(row=2,column=1)
    t2.grid(row=2,column=2)
    b1.grid(row=5,column=2)
    b2.grid(row=5,column=3)
    window.mainloop()        
        

