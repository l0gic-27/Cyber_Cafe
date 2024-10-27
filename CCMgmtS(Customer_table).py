#CCMgmtS(Customer_Table)

import mysql.connector as mycon
con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
if con.is_connected():
    print("Connection Success")
c1=con.cursor()
c1.execute("create table New_Customer(ID int PRIMARY KEY NOT NULL AUTO_INCREMENT, Customer_Name varchar(25), Phone_no int(10) ,Email varchar(25))")
print("Table created")


