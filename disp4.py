import mysql.connector as mycon
con=mycon.connect(
    host="localhost",
    user="root",
    password="7869009019@#",
    db="sundaydb",
)
mycur=con.cursor()
name=input("enter name")
age=input("enter age")
salary=input("enter salary")
mycur.execute("update emp set name=%s,age=%s,salary=%s",[name,age,salary])
mycon.commit()
print("Record updated.....")