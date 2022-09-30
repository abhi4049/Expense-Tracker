
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('SIGN UP')
root.geometry("600x400")
root.configure(bg="beige")
t=Text(root, width=40, height= 1, font=("Times", "30", "bold"), fg="white", bg="blue", wrap=WORD)
t.insert(END,"EXPENSE TRACKER")
t.pack(side=TOP)
f2=Frame(root, bg="black",padx=90,pady=30)
f2.pack()
def signup():
    f2=Frame(bg="black")
    f2.place(width=600, height=400)
    f2=Toplevel()
    f2.title("SIGNUP")

    l1=Label(f2,text='Username:',width=14,height=1, font=("Times", "14", "bold"))
    l2=Label(f2,text='Password:',width=14,height=1, font=("Times", "14", "bold"),pady=10)
    l3=Label(f2,text='Confirm Password:',width=14,height=1, font=("Times", "14", "bold"),pady=10)
    l4=Label(f2,text='Age:',width=14,height=1, font=("Times", "14", "bold"),pady=10)
    l5=Label(f2,text='Gender:',width=14,height=1, font=("Times", "14", "bold"),pady=10)
    l6=Label(f2,text='Mobile Number:',width=14,height=1, font=("Times", "14", "bold"),pady=10)
    
    e1=Entry(f2,width=14,font=("Times", "14", "bold"))
    e2=Entry(f2,width=14,show='*', font=("Times", "14", "bold"))
    e3=Entry(f2,width=14,show='*',font=("Times", "14", "bold"))
    e4=Entry(f2,width=14, font=("Times", "14", "bold"))
    
    i=StringVar()
   
    r1=Radiobutton(f2,text='Male', value="male", variable=i, font=("Times", "14", "bold"),bg="yellow", activebackground="magenta")
    r2=Radiobutton(f2,text='Female',value="female", variable=i, font=("Times", "14", "bold"),bg="yellow", activebackground="magenta")
    
    e6=Entry(f2,width=14, font=("Times", "14", "bold"))
    
    e1.get()
    e2.get()
    e3.get()
    e4.get()
    e6.get()

    username=e1.get()
    age=e4.get()
    gender=i.get()
    mobile_no=e6.get()
    pwd=e3.get()

    import mysql.connector as c
    con=c.connect(host='localhost', user='root', passwd='abhimysql@13B', database='expense')
    cursor=con.cursor()
    query="Insert into signup values('{}', {}, '{}', {}, '{}')".format(username,age,gender,mobile_no,pwd)

    cursor.execute(query)
    con.commit()

    b1=Button(f2,text='ADD ACCOUNT',width=15,height=3, bg="dodgerblue", activebackground="azure",)
    b2=Button(f2,text='BACK',width=15,height=3, bg="orangered", activebackground="azure", command=home)

    l1.grid(row=0,column=0)
    e1.grid(row=0,column=3)
    l2.grid(row=1,column=0)
    e2.grid(row=1,column=3)
    l3.grid(row=2,column=0)
    e3.grid(row=2,column=3)
    l4.grid(row=3,column=0)
    e4.grid(row=3,column=3)
    l5.grid(row=5,column=0)
    r1.grid(row=5,column=2)
    r2.grid(row=5,column=3)
    l6.grid(row=7,column=0)
    e6.grid(row=7,column=3)
    b1.grid(row=9,column=0)
    b2.grid(row=9,column=3)

def home():
    f=Frame(bg="black")
    f.place(width=600, height=400)
    b1=Button(f,text='EXISTING USER',width=20,height=3, bg="green2", activebackground="aquamarine")
    b2=Button(f,text='NEW USER',width=20,height=3, bg="coral", activebackground="aquamarine", command =signup)
    b3=Button(f,text='EXIT',width=20,height=3, bg="red", activebackground="aquamarine", command =f.destroy)
    b1.grid(row=1,column=0,padx=30)
    b2.grid(row=1,column=1,padx=30)
    b3.grid(row=2,column=0,padx=30)
    f.pack()
home()
t.mainloop()
