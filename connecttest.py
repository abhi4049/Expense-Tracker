import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="abhimysql@13B", database="dummy")
cursor=con.cursor()
x=1
while (x==1):
    code=int(input("Enter code: "))
    name=input("Enter name: ")
    salary=int(input("Enter Salary: "))
    query="Insert into sample values({}, '{}', {})".format(code,name,salary)
    cursor.execute(query)
    con.commit()
    print("Data inserted successfully ...")
    x=int(input("1. Enter Again\n2. Exit\nEnter your choice: "))
