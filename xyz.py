import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "abhimysql@13B",database = "expense",)

window = Tk()
window.title("PYTROOPS")
window.geometry("300x300")
window.configure(background = "yellow")


from tkinter import ttk

def delete():
    get_c1 = c1.get()
    get_E1 = E1.get()

    cur = mydb.cursor()
    delt = "DELETE from inex where %s='%s'"%(get_c1,get_E1)
    cur.execute(delt)
    mydb.commit()

val = ['username' ,'dt', 'bname', 'category','income_expense', 'amount', 'pmode']
c1 = ttk.Combobox(window , value = val)
c1.grid(row = 0 , column = 0 , padx = 10 , pady = 10)

E1 = Entry(window)
E1.grid(row = 0 , column = 1)
btn = Button(window, text = 'Delete' , command = delete )
btn.grid(row = 1 , column = 0, padx = 10, pady = 10)

window.mainloop()