from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('ADD INCOME/EXPENSE')
root.geometry("600x400")
root.configure(bg="beige")
t=Text(root, width=40, height= 1, font=("Times", "30", "bold"), fg="white", bg="blue", wrap=WORD)
t.insert(END,"EXPENSE TRACKER")
t.pack(side=TOP)
f=Frame(root, bg="black",padx=60,pady=20)
f.pack()


def addie():
    e1.get()
    e2.get()
    e3.get()
    e4.get()
    
    e6.get()
    
l1=Label(f,text='Date',width=14,height=1, font=("Times", "14", "bold"),pady=5)
l2=Label(f,text='Beneficiary Name',width=14,height=1, font=("Times", "14", "bold"),pady=5)
l3=Label(f,text='Category:',width=14,height=1, font=("Times", "14", "bold"),pady=5)
l4=Label(f,text='Amount (in ₹):',width=14,height=1, font=("Times", "14", "bold"),pady=5)
l5=Label(f,text='Mode:',width=14,height=1, font=("Times", "14", "bold"),pady=5)

var=IntVar()
var.set(2)
r1=Radiobutton(f,text='Income',variable=var,value=1, font=("Times", "14", "bold"),bg="yellow", activebackground="magenta")
r2=Radiobutton(f,text='Expense',variable=var,value=2, font=("Times", "14", "bold"),bg="yellow", activebackground="magenta")
e1=Entry(f,width=14,font=("Times", "14", "bold"))
e2=Entry(f,width=14,show='*', font=("Times", "14", "bold"))
e3=Entry(f,width=14,show='*',font=("Times", "14", "bold"))
e4=Entry(f,width=14, font=("Times", "14", "bold"))

sp= Spinbox(f, values=('Card', 'Cash', 'Netbanking', 'Salary'),textvariable=StringVar, width=13,font=("Times", "14", "bold"))
e6=Entry(f,width=14, font=("Times", "14", "bold"))
b1=Button(f,text='ADD ACCOUNT',width=15,height=2, bg="dodgerblue", activebackground="azure")
b2=Button(f,text='BACK',width=15,height=2, bg="orangered", activebackground="azure")

r1.grid(row=0,column=0,pady=10)
r2.grid(row=0,column=3,pady=10)

l1.grid(row=1,column=0)
e1.grid(row=1,column=3)
l2.grid(row=2,column=0)
e2.grid(row=2,column=3)
l3.grid(row=3,column=0)
e3.grid(row=3,column=3)
l4.grid(row=4,column=0)
e4.grid(row=4,column=3)
l5.grid(row=5,column=0)
sp.grid(row=5,column=3)

b1.grid(row=7,column=1,pady=20)
b2.grid(row=7,column=3,pady=20)



root.mainloop()