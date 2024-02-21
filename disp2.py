import mysql.connector as mycon
con=mycon.connect(
    host="localhost",
    user="root",
    password="7869009019@#",
    db="sundaydb"
)
mycur=con.cursor()
mycur.execute("select * from emp")
data=mycur.fetchall()
for item in data:
    print(item[0],"\t",item[1],"\t",item[2])
    