from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('LOGIN')
root.geometry("600x400")
root.configure(bg="beige")
t=Text(root, width=40, height= 1, font=("Times", "30", "bold"), fg="white", bg="blue", wrap=WORD)
t.insert(END,"EXPENSE TRACKER")
t.pack(side=TOP)
f1=Frame(root, bg="black",padx=100,pady=90)
f1.pack()

def login():
    s1=e1.get()
    s2=e2.get()
    if s1=='SAYS' and s2=='SAYS':
        messagebox.showinfo('Welcome','Successful Login...')
    else:
        messagebox.showerror('Error','Invalid User...') 

l1=Label(f1,text='Username:',width=14, height=1, font=("Times", "14", "bold"))
l2=Label(f1,text='Password:',width=14, height=1, font=("Times", "14", "bold"))

e1=Entry(f1,width=14,font=("Times", "15", "bold"))
e2=Entry(f1,width=14,show='*',font=("Times", "15", "bold"))

b1=Button(f1,text='Login',width=20,height=3, bg="green2", activebackground="aquamarine", command=login)
b2=Button(f1,text='BACK',width=20,height=3, bg="orangered", activebackground="azure")

l1.grid(row=0,column=0,padx=10)
e1.grid(row=0,column=2)
l2.grid(row=1,column=0,pady=10,padx=10)
e2.grid(row=1,column=2)
b1.grid(row=2,column=0,pady=20)
b2.grid(row=2,column=2)


root.mainloop()





