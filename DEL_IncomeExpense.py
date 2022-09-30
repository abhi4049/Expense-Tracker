from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('LOGIN')
root.geometry("600x400")
root.configure(bg="beige")
t=Text(root, width=40, height= 1, font=("Times", "30", "bold"), fg="white", bg="blue", wrap=WORD)
t.insert(END,"EXPENSE TRACKER")
t.pack(side=TOP)
f=Frame(root, bg="black",padx=100,pady=90)
f.pack()

root.mainloop()