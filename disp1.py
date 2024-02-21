import mysql.connector as mycon
con=mycon.connect(
   host="localhost",
   user="root",
   password="7869009019@#",
   db="sundaydb"

)
mycur=con.cursor()
name=input("enter name")
age=input("enter age")
salary=input("enter salary")
mycur.execute("insert into emp(name,age,salary) values (%s,%s,%s)",[name,age,salary])
con.commit()
print("Inserted Record....")