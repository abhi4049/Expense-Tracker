from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('LOGIN')
root.geometry("600x400")
root.configure(bg="beige")
t=Text(root, width=40, height= 1, font=("Times", "30", "bold"), fg="white", bg="blue", wrap=WORD)
t.insert(END,"EXPENSE TRACKER")
t.pack(side=TOP)
t=Text(root, width=100, height= 25, font=("Times", "10"), fg="white", bg="black", wrap=WORD)
t.insert(END,"abcd")
t.pack(side=TOP)
s=Scrollbar(root, orient=VERTICAL,command=t.yview)
t.configure(yscrollcommand=s.set)
s.pack(side=RIGHT, fill=Y)
f=Frame(root, bg="black",padx=100,pady=120)
f.pack()

root.mainloop()