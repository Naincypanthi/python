import mysql.connector as mycon
con=mycon.connect(
    host="localhost",
    user="root",
    password="7869009019@#",
    db="sundaydb",
)
mycur=con.cursor()
name=input("enter name")
mycur.execute("delete from emp where name=%s",[name])
con.commit()
print("record deleted")