import tkinter
import os	
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.messagebox import *
from tkinter.filedialog import *
from typing import AsyncGenerator
from datetime import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import ttk
t=Tk()
t.title('EXPENSE TRACKER')
t.geometry("600x400")
t.configure(bg="beige")
t=Text(t, width=40, height= 1, font=("Arial serif", "30", "bold"), fg="navy", bg="#45aaf2", wrap=WORD)
t.insert(END,"EXPENSE TRACKER")
t.pack(side=TOP)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def login():
    f1=Frame(bg="#45aaf2",padx=125,pady=60)
    f1.place(width=600, height=400)
    
   
    l1=Label(f1,text='Username:',width=14, height=1, font=("Arial serif", "14", "bold"))
    l2=Label(f1,text='Password:',width=14, height=1, font=("Arial serif", "14", "bold"))
    e1=Entry(f1,width=14,font=("Arial serif", "15", "bold"))
    e2=Entry(f1,width=14,show='*',font=("Arial serif", "15", "bold"))
    

    def verify():
        e1.get()
        e2.get()
        import mysql.connector as c
        con=c.connect(host='localhost', user='root', passwd='abhimysql@13B', database='expense')
        cursor=con.cursor()
        cursor.execute("select pwd from signup")
        record=cursor.fetchall()
        for i in record:
            if i[0]==e2.get():
                tmsg.showinfo("Login", "Login Successful ...")
        else:
            tmsg.showinfo("Login Unsuccessful", "Please, enter valid credentials!")

    b1=Button(f1,text='LOGIN',width=15,height=2,fg="white", bg="blue", activebackground="lightyellow",font=("Arial serif", "12", "bold"),command=verify)
    b2=Button(f1,text='BACK',width=15,height=2,fg="white", bg="red", activebackground="lightyellow",font=("Arial serif", "12", "bold"),command=f1.destroy)
    b3=Button(f1,text='PROCEED',width=15,height=2,fg="black", bg="green2", activebackground="lightyellow",font=("Arial serif", "12", "bold"), command=menu)
    l1.grid(row=0,column=0,padx=10)
    e1.grid(row=0,column=2)
    l2.grid(row=1,column=0,pady=10,padx=10)
    e2.grid(row=1,column=2)
    b1.grid(row=2,column=0,pady=20)
    b2.grid(row=2,column=2,pady=20)
    b3.grid(row=3,column=0)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def signup():
    f2=Frame(bg="#45aaf2",padx=115,pady=40)
    f2.place(width=600, height=400)
    
    username=StringVar
    pwd=StringVar
    age=StringVar
    mobile_no=StringVar
    

    l1=Label(f2,text='Username:',width=14,height=1, font=("Arial serif", "14", "bold"))
    l2=Label(f2,text='Password:',width=14,height=1, font=("Arial serif", "14", "bold"),pady=10)
    l3=Label(f2,text='Confirm Password:',width=14,height=1, font=("Arial serif", "14", "bold"),pady=10)
    l4=Label(f2,text='Age:',width=14,height=1, font=("Arial serif", "14", "bold"),pady=10)
    l5=Label(f2,text='Gender:',width=14,height=1, font=("Arial serif", "14", "bold"),pady=10)
    l6=Label(f2,text='Mobile Number:',width=14,height=1, font=("Arial serif", "14", "bold"),pady=10)
    
    e1=Entry(f2,textvariable="username",width=14,font=("Arial serif", "14", "bold"))
    e2=Entry(f2,width=14,show='*', font=("Arial serif", "14", "bold"))
    e3=Entry(f2,width=14,textvariable="pwd",show='*',font=("Arial serif", "14", "bold"))
    e4=Entry(f2,width=14,textvariable="age",font=("Arial serif", "14", "bold"))
    
    i=StringVar()
   
    r1=Radiobutton(f2,text='Male', value="male", variable=i, font=("Arial serif", "14", "bold"),bg="lightyellow", activebackground="dodger blue")
    r2=Radiobutton(f2,text='Female',value="female", variable=i, font=("Arial serif", "14", "bold"),bg="lightyellow", activebackground="hotpink")
    
    e6=Entry(f2,textvariable=" mobile_no",width=14, font=("Arial serif", "14", "bold"))
    
    e1.get()
    e2.get()
    e3.get()
    e4.get()
    e6.get()

   

    def signpro():
        if e2.get()==e3.get():
            username=e1.get()
            age=int(e4.get())
            gender=i.get()
            mobile_no=int(e6.get())
            pwd=e3.get()
            import mysql.connector as c
            con=c.connect(host='localhost', user='root', passwd='abhimysql@13B', database='expense')
            cursor=con.cursor()
            query="Insert into signup values(%s, %s, %s, %s, %s)"
            tup=(username,age,gender,mobile_no,pwd)
            cursor.execute(query,tup)
            con.commit()
            tmsg.showinfo("SIGNUP", "Signup Successful ...")
        else:
            tmsg.showinfo("SIGNUP Signup Unsuccessful ...", "Password and Confirm Password are not same")

        
    b1=Button(f2,text='ADD ACCOUNT',width=15,height=2,fg="white", bg="blue", activebackground="lightyellow",font=("Arial serif", "12", "bold"), command=signpro)
    b2=Button(f2,text='BACK',width=15,height=2,fg="white", bg="red", activebackground="lightyellow", font=("Arial serif", "12", "bold"), command=f2.destroy)

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
    b1.grid(row=9,column=0,pady=15)
    b2.grid(row=9,column=3,pady=15)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def menu():
    f3=Frame(bg="#45aaf2",padx=70,pady=60)
    f3.place(width=600, height=400)
    
    b1=Button(f3,text='DASHBOARD',width=23,height=2, bg="green2", activebackground="azure",font=("Arial serif", "12", "bold"),command=dash)
    b2=Button(f3,text='ADD INCOME/EXPENSE',width=23,height=2, bg="orange", activebackground="azure",font=("Arial serif", "12", "bold"), command=addie)
    b3=Button(f3,text='STATISTICS',width=23,height=2, bg="orange",font=("Arial serif", "12", "bold"), activebackground="azure",command=stats)
    b4=Button(f3,text='DELETE INCOME/EXPENSE',width=23,height=2, bg="green2", activebackground="azure",font=("Arial serif", "12", "bold"), command=delie)
    b5=Button(f3,text='NOTES',width=23,height=2,bg="green2", activebackground="azure",font=("Arial serif", "12", "bold"),command=notes)
    b6=Button(f3,text='USERS',width=23,height=2, bg="orange", activebackground="azure",font=("Arial serif", "12", "bold"),command=users)
    b7=Button(f3,text='FAQs',width=23,height=2,fg="white", bg="blue", activebackground="lightyellow",font=("Arial serif", "12", "bold"),command=faqs)
    b8=Button(f3,text='LOGOUT!',width=23,height=2,fg="white", bg="red", activebackground="lightyellow",font=("Arial serif", "12", "bold"), command=login)
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1,padx=20)
    b3.grid(row=2,column=0,pady=10)
    b4.grid(row=2,column=1,pady=10)
    b5.grid(row=4,column=0,pady=10)
    b5.grid(row=4,column=0,pady=10)
    b6.grid(row=4,column=1,pady=10)
    b7.grid(row=6,column=0,pady=10)
    b8.grid(row=6,column=1,pady=10)
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def addie():
    f4=Frame(bg="#45aaf2",padx=110,pady=30)
    f4.place(width=600, height=400)
    username=StringVar
    dt=StringVar
    bname=StringVar
    amount=StringVar
    category=StringVar
    pmode=StringVar
    income_expense=StringVar
    l1=Label(f4,text='Username:',width=14,height=1, font=("Arial serif", "14", "bold"),pady=5)
    l2=Label(f4,text='Date (yy/mm/dd)',width=14,height=1, font=("Arial serif", "14", "bold"),pady=5)
    l3=Label(f4,text='Name',width=14,height=1, font=("Arial serif", "14", "bold"),pady=5)
    l4=Label(f4,text='Category:',width=14,height=1, font=("Arial serif", "14", "bold"),pady=5)
    l5=Label(f4,text='Amount (in ₹):',width=14,height=1, font=("Arial serif", "14", "bold"),pady=5)
    l6=Label(f4,text='Mode:',width=14,height=1, font=("Arial serif", "14", "bold"),pady=5)
    
    i=StringVar()
   
    r1=Radiobutton(f4,text='Income', value="income", variable=i, font=("Arial serif", "14", "bold"),bg="lightyellow", activebackground="green2")
    r2=Radiobutton(f4,text='Expense',value="expense", variable=i, font=("Arial serif", "14", "bold"),bg="lightyellow", activebackground="orange")
    e1=Entry(f4,width=14,textvariable="username", font=("Arial serif", "14", "bold"))
    e2=Entry(f4,width=14,textvariable="dt", font=("Arial serif", "14", "bold"))
    e3=Entry(f4,width=14,textvariable="bname", font=("Arial serif", "14", "bold"))
    spin1= Spinbox(f4, textvariable=StringVar, values=('Food', 'Education', 'Medical', 'Travel', 'Entertainment', 'Bills', 'Grocery', 'Personal', 'Salary', 'Miscellaneous'), width=13,font=("Arial serif", "14", "bold"))
    e4=Entry(f4,width=14,textvariable="amount",font=("Arial serif", "14", "bold"))
    spin2= Spinbox(f4, textvariable=StringVar, values=('Cash', 'Card', 'UPI', 'NEFT', 'RTGS', 'IMPS', 'Salary'), width=13,font=("Arial serif", "14", "bold"))
  

    def addiepro():
        username=e1.get()
        dt=e2.get()
        bname=e3.get()
        category=spin1.get()
        income_expense=i.get()
        amount=int(e4.get())
        pmode= spin2.get()
        import mysql.connector as c
        con=c.connect(host='localhost', user='root', passwd='abhimysql@13B', database='expense')
        cursor=con.cursor()
        query="Insert into inex values(%s, %s, %s, %s, %s, %s, %s)"
        tup=(username, dt, bname, category, income_expense, amount, pmode)
        cursor.execute(query,tup)
        con.commit()
        tmsg.showinfo("ADD Income/Expense", "Added successfully ...")

    
    b1=Button(f4,text='ADD INOME/EXPENSE',width=20,height=2,fg="white", bg="blue", activebackground="lightyellow",font=("Arial serif", "12", "bold"),command=addiepro)
    b2=Button(f4,text='BACK',width=15,height=2,fg="white", bg="red", activebackground="lightyellow",font=("Arial serif", "12", "bold"), command=menu)

    r1.grid(row=0,column=0,pady=10)
    r2.grid(row=0,column=2,pady=10)

    l1.grid(row=1,column=0)
    e1.grid(row=1,column=2)
    l2.grid(row=2,column=0)
    e2.grid(row=2,column=2)
    l3.grid(row=3,column=0)
    e3.grid(row=3,column=2)
    l4.grid(row=4,column=0)
    spin1.grid(row=4,column=2)
    l5.grid(row=5,column=0)
    e4.grid(row=5,column=2)
    l6.grid(row=6,column=0)
    spin2.grid(row=6,column=2)


    b1.grid(row=7,column=0,pady=20)
    b2.grid(row=7,column=2,pady=20,padx=40)
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------
def delie():
    f9=Frame(bg="#45aaf2",padx=85,pady=50)
    f9.place(width=600, height=400)
    val = ['username' ,'dt', 'bname', 'category','income_expense', 'amount', 'pmode']
    c1 = ttk.Combobox(f9, value = val)
    E1 = Entry(f9,width=14,textvariable="username", font=("Arial serif", "14", "bold"))
    def deliepro():
        get_c1 = c1.get()
        get_E1 = E1.get()

        import mysql.connector as c
        mydb = c.connect(host = "localhost", user = "root", passwd = "abhimysql@13B",database = "expense",)
        cur = mydb.cursor()
        delt = "DELETE from inex where %s='%s'"%(get_c1,get_E1)
        cur.execute(delt)
        mydb.commit()
        
        
    E1.grid(row = 0 , column = 1)
    b1=Button(f9,text='REMOVE INOME/EXPENSE',width=25,height=2,fg="white", bg="blue", activebackground="lightyellow",font=("Arial serif", "12", "bold"),command=deliepro)
    b2=Button(f9,text='BACK',width=15,height=2,fg="white", bg="red", activebackground="lightyellow",font=("Arial serif", "12", "bold"), command=menu)
    c1.grid(row=1,column=0)
    E1.grid(row=1,column=2)
    b1.grid(row=4,column=0,pady=140)
    b2.grid(row=4,column=2,pady=140,padx=40)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def faqs():
    
    f5=Toplevel()
    f5.geometry=("100x100+100+100")
    
    t=Text(f5, width=50, height=35, font=("Arial serif", "14", "bold", "italic"), fg='darkblue', bg='white', wrap=WORD)
    t.insert(END, "1. How to 'Sign Up'?\nIf you are a new user click on the new user button. It takes you to the sign up page. On the sign up page enter your 'username' ,'password','confirm password' ,'Age','Gender','Mobile Number'. After entering all your credentials,  click on the 'Add account' button. After clicking on the Add account button a message pops up which informs about MSG.\n2. How to 'Login'?\nIf You are an existing user , then click on the 'existing user' button. It takes you to the Login Page . On the login page enter your 'username' and 'password'. After entering all your credentials, click on the 'Login 'button. After clicking on the Login button a message is generated of successful  login then clicking on the ' Proceed' button . It takes you to 'Menu' page.\n3. How does the 'Dashboard' button work?\nDashboard displays the information of the last five  transactions performed by the user. It consists of ‘username’, ‘date’, ’name, ’category’, ’income/expense’, amount and mode of payment. \n4. How to Add Income/Expense ?\nClick on the 'Add Income/Expense' button. If you want to add income select 'Income Or for expense select 'Expense'.Now enter 'username' ,'date in the form of (YY/MM/DD)', 'name' and preset 'categories' of transaction,its 'amount' and preset 'payment modes'.After that click on 'Add Income/Expense Button. A message informing about the addition l of income/expense will be displayed on the screen.\n5. How does the 'Statistics' button work?\nStatistics button displays a pie-chart formed by category and amount.\n6. How to Delete Income/Expense?\nClick on Delete Income/Expense button.To delete income/expense Enter values of  any of username,date,name category,income/expense,amount,payment modes in the entry  widget.\nNow click on the Remove Income/Expense button. A message informing about the removal of income/expense will be displayed on the screen.\n7. What is ‘Notes’?\nNotes is a special feature in the menu that provides an option note down a few important things before entering them. It has three menus viz. File, Edit and About. File menu contains New, Open, Save and Exit. New option allows us to create a new note. Open option opens an already existing note. Save option saves working unsaved notes. Exit option facilitates exit from Notes.Edit menu contains  Cut, Copy and Paste. Cut option allows you to cut a portion of a sentence. Copy option allows you to copy a portion of a sentence. Paste option facilitates pasting of already cut and copied portions of sentence. About option displays information about Notes. \n8. What is ‘Users’?\nUsers button displays non-confidential information pertaining to all the users who have signed up into the application.\n9. What are FAQs?\nFAQs stands for Frequently Asked Questions. FAQs consist of the most common possible issues that naive users might face while using this  application. They facilitate smooth,easier and faster access to the application.\n10. What is ‘Logout’?\nLogout logs you out of the application and takes you to the login page.")

    t.pack(side=TOP)
   
    
    s=Scrollbar(f5, bg="black", orient=VERTICAL, command=t.yview)
    s.pack(side=RIGHT, fill=Y)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def dash():
    f7=Frame(bg="#45aaf2",padx=20,pady=70)
    f7.place(width=600, height=400)
    l1=Label(f7,text="Username: " ,width=11,height=1, font=("Arial serif", "10", "bold"))
    l2=Label(f7,text="Date: " ,width=11,height=1, font=("Arial serif", "10", "bold"))
    l3=Label(f7,text='Name: ',width=11, height=1, font=("Arial serif", "10", "bold"))
    l4=Label(f7,text='Category: ',width=11,height=1, font=("Arial serif", "10", "bold"))
    l5=Label(f7,text='Income/Expense: ',width=13,height=1, font=("Arial serif", "10", "bold"))
    l6=Label(f7,text='Amount (in ₹): ',width=11,height=1, font=("Arial serif", "10", "bold"))
    l7=Label(f7,text='Mode: ',width=11,height=1, font=("Arial serif", "10", "bold"))
    tmsg.showinfo("DASHBOARD", "Displaying last 5 transactions ...")

    import mysql.connector as c
    con=c.connect(host='localhost', user='root', passwd='abhimysql@13B', database='expense')
    cursor=con.cursor()
    cursor.execute("SELECT * FROM inex limit 0,5")
    i=0 
    for inex in cursor: 
        for j in range(len(inex)):
            e = Entry(f7, width=13, fg='blue') 
            e.grid(row=i+2, column=j) 
            e.insert(END, inex[j])
        i=i+1

    
    b1=Button(f7,text='BACK',width=10,height=2,fg="white", bg="red", activebackground="lightyellow",font=("Arial serif", "10", "bold"),command=menu) 
    
    l1.grid(row=1,column=0)
    l2.grid(row=1,column=1)
    l3.grid(row=1,column=2)
    l4.grid(row=1,column=3)
    l5.grid(row=1,column=4)
    l6.grid(row=1,column=5)
    l7.grid(row=1,column=6)
    b1.grid(row=10,column=0,pady=15)     
   
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def users():
    f8=Frame(bg="#45aaf2",padx=20,pady=70)
    f8.place(width=600, height=400)
    l1=Label(f8,text="Username: " ,width=14,height=1, font=("Arial serif", "12", "bold"),justify=CENTER)
    l2=Label(f8,text="Age " ,width=14,height=1, font=("Arial serif", "12", "bold"),justify=CENTER)
    l3=Label(f8,text='Gender: ',width=14, height=1, font=("Arial serif", "12", "bold"),justify=CENTER)
    l4=Label(f8,text='Mobile No: ',width=14,height=1, font=("Arial serif", "12", "bold"),justify=CENTER)

    import mysql.connector as c
    con=c.connect(host='localhost', user='root', passwd='abhimysql@13B', database='expense')
    cursor=con.cursor()
    cursor.execute("SELECT username, age, gender, mobile_no FROM signup limit 0,5")
    i=0 
    for signup in cursor: 
        for j in range(len(signup)):
            e = Entry(f8, width=17, fg='blue', font=("Arial serif", "11", "bold"), justify=CENTER) 
            e.grid(row=i+2, column=j) 
            e.insert(END, signup[j])
        i=i+1
    b1=Button(f8,text='BACK',width=10,height=2,fg="white", bg="red", activebackground="lightyellow",command=menu,font=("Arial serif", "12", "bold"), justify=CENTER) 
    
    l1.grid(row=1,column=0)
    l2.grid(row=1,column=1)
    l3.grid(row=1,column=2)
    l4.grid(row=1,column=3)
    b1.grid(row=10,column=0,pady=15) 

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def stats():
    f9=Frame(bg="#45aaf2",padx=125,pady=60)
    f9.place(width=600, height=400)
        
    df = pd.read_csv('stats.csv')
    plt.style.use('bmh')

    x = df['category']
    y = df['amount']

    plt.pie(y, labels=x, radius=1.2, autopct='%0.01f%%', shadow = True)
    plt.show()
    b1=Button(f9,text='BACK',width=10,height=2,fg="white", bg="red", activebackground="lightyellow",command=menu,font=("Arial serif", "12", "bold"), justify=CENTER) 
    b1.grid(row=0,column=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

class Notepad:

	__root = Tk()

	# default window width and height
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(__root)
	__thisMenuBar = Menu(__root)
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0)
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
	
	# To add scrollbar
	__thisScrollBar = Scrollbar(__thisTextArea)	
	__file = None

	def __init__(self,**kwargs):

		# Set icon
		try:
				self.__root.wm_iconbitmap("Notepad.ico")
		except:
				pass

		# Set window size (the default is 300x300)

		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			pass

		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			pass

		# Set the window text
		self.__root.title("Untitled - Note")

		# Center the window
		screenWidth = self.__root.winfo_screenwidth()
		screenHeight = self.__root.winfo_screenheight()
	
		# For left-alling
		left = (screenWidth / 2) - (self.__thisWidth / 2)
		
		# For right-allign
		top = (screenHeight / 2) - (self.__thisHeight /2)
		
		# For top and bottom
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
											self.__thisHeight,
											left, top))

		# To make the textarea auto resizable
		self.__root.grid_rowconfigure(0, weight=1)
		self.__root.grid_columnconfigure(0, weight=1)

		# Add controls (widget)
		self.__thisTextArea.grid(sticky = N + E + S + W)
		
		# To open new file
		self.__thisFileMenu.add_command(label="New",
										command=self.__newFile)	
		
		# To open a already existing file
		self.__thisFileMenu.add_command(label="Open",
										command=self.__openFile)
		
		# To save current file
		self.__thisFileMenu.add_command(label="Save",
										command=self.__saveFile)	

		# To create a line in the dialog		
		self.__thisFileMenu.add_separator()										
		self.__thisFileMenu.add_command(label="Exit",
										command=self.__quitApplication)
		self.__thisMenuBar.add_cascade(label="File",
									menu=self.__thisFileMenu)	
		
		# To give a feature of cut
		self.__thisEditMenu.add_command(label="Cut",
										command=self.__cut)			
	
		# to give a feature of copy	
		self.__thisEditMenu.add_command(label="Copy",
										command=self.__copy)		
		
		# To give a feature of paste
		self.__thisEditMenu.add_command(label="Paste",
										command=self.__paste)		
		
		# To give a feature of editing
		self.__thisMenuBar.add_cascade(label="Edit",
									menu=self.__thisEditMenu)	
		
		# To create a feature of description of the notepad
		self.__thisHelpMenu.add_command(label="About Notepad",
										command=self.__showAbout)
		self.__thisMenuBar.add_cascade(label="Help",
									menu=self.__thisHelpMenu)

		self.__root.config(menu=self.__thisMenuBar)

		self.__thisScrollBar.pack(side=RIGHT,fill=Y)					
		
		# Scrollbar will adjust automatically according to the content		
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
	
		
	def __quitApplication(self):
		self.__root.destroy()
		# exit()

	def __showAbout(self):
		showinfo("Notepad","Expense Tracker")

	def __openFile(self):
		
		self.__file = askopenfilename(defaultextension=".txt",
									filetypes=[("All Files","*.*"),
										("Text Documents","*.txt")])

		if self.__file == "":
			
			# no file to open
			self.__file = None
		else:
			
			# Try to open the file
			# set the window title
			self.__root.title(os.path.basename(self.__file) + " - Notepad")
			self.__thisTextArea.delete(1.0,END)

			file = open(self.__file,"r")

			self.__thisTextArea.insert(1.0,file.read())

			file.close()

		
	def __newFile(self):
		self.__root.title("Untitled - Notepad")
		self.__file = None
		self.__thisTextArea.delete(1.0,END)

	def __saveFile(self):

		if self.__file == None:
			# Save as new file
			self.__file = asksaveasfilename(initialfile='Untitled.txt',
											defaultextension=".txt",
											filetypes=[("All Files","*.*"),
												("Text Documents","*.txt")])

			if self.__file == "":
				self.__file = None
			else:
				
				# Try to save the file
				file = open(self.__file,"w")
				file.write(self.__thisTextArea.get(1.0,END))
				file.close()
				
				# Change the window title
				self.__root.title(os.path.basename(self.__file) + " - Notepad")
				
			
		else:
			file = open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()

	def __cut(self):
		self.__thisTextArea.event_generate("<<Cut>>")

	def __copy(self):
		self.__thisTextArea.event_generate("<<Copy>>")

	def __paste(self):
		self.__thisTextArea.event_generate("<<Paste>>")

	def run(self):

		# Run main application
		self.__root.mainloop()




# Run main application
def notes():
    Notepad(width=600,height=400)
    notes.run()

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def home():
    f=Frame(bg="#45aaf2",padx=37,pady=145)    
    f.place(width=600, height=400)
    b1=Button(f,text='EXISTING USER',width=16,height=3, fg="white", bg="blue", activebackground="lightyellow",bd=0.5,font=("Arial serif", "11", "bold"), command=login)
    b2=Button(f,text='NEW USER',width=16,height=3, fg="white", bg="darkgreen", activebackground="lightyellow",bd=0.5,font=("Arial serif", "11", "bold"), command =signup)
    b3=Button(f,text='EXIT',width=16,height=3, fg="white", bg="red", activebackground="lightyellow",bd=0.5,font=("Arial serif", "11", "bold"), command =f.destroy)
    
    b1.grid(row=1,column=0,padx=10)
    b2.grid(row=1,column=1,padx=20)
    b3.grid(row=1,column=2,padx=10)
    f.pack()

home()
t.mainloop()
