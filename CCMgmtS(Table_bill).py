import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="root",database="ccmgmts")
if con.is_connected():
    print("Connection Success")
c1=con.cursor()
c1.execute("create Table Bill(Customer_Name varchar(20), Accessed_Time int, Total_Bill int)")
print("Table created")

"""
username = input("Enter Your Username(Admins Only):- \n")
        password = input("Enter Your Password(Admins Only):- \n")
        usname = 'ccmgmts'
        passwd = 'cafe'

        if(username == usname) and (password == passwd):
            print("-----------------------")
            print("-----WELCOME ADMIN-----")
            print("----------------------- \n")
            print("1.Update Employee Details.")
            print("2.Delete Employee Data.")
            print("3.View Employee Details.")
            print("4.Exit. \n")

            Choice=int(input("Enter Your Choice:- \n"))

            if Choice==1:
                print("-----------------------")
                print("-----WELCOME ADMIN----- \n")
                print("1.FullName")
                print("2.Age.")
                print("3.Designation.")
                print("4.Salary.")
                print("5.Email.")
                print("6.Exit.")

                Choice=int(input("Enter Your Choice:-"))

                con = mycon.connect(host="localhost", user="root", password="root", database="ccmgmts")

                if con.is_connected():
                    print("Connection Success")
                c1 = con.cursor()
                c1.execute("Select * from emp")

                if Choice==1:
                    data=c1.fetchall()
                    a=input("Enter Name:-")
                    b=input("Enter EmpID:-")
                    st="UPDATE emp Set FullName = '{}' where EmpId = '{}'".format(a,b)

                    c1.execute(st)
                    con.commit()
                    con.close()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                if Choice==2:
                    data=c1.fetchall()
                    a=input("Enter Age:-")
                    b=input("Enter EmpID:-")
                    st="UPDATE emp Set Age = '{}' where EmpID = '{}'".format(a,b)

                    c1.execute(st)
                    con.commit()
                    con.close()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                if Choice==3:
                    data=c1.fetchall()
                    a=input("Enter Designation:-")
                    b=input("Enter EmpID:-")
                    st="UPDATE emp Set Designation = '{}' where EmpID = '{}'".format(a,b)

                    c1.execute(st)
                    con.commit()
                    con.close()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                if Choice==4:
                    data=c1.fetchall()
                    a=input("Enter Salary:-")
                    b=input("Enter EmpID:-")
                    st="UPDATE emp Set Salary = '{}' where EmpID = '{}'".format(a,b)

                    c1.execute(st)
                    con.commit()
                    con.close()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                if Choice==5:
                    data=c1.fetchall()
                    a=input("Enter Email:-")
                    b=input("Enter EmpID:-")
                    st="UPDATE emp Set Email = '{}' where EmpId = '{}'".format(a,b)

                    c1.execute(st)
                    con.commit()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                if Choice==6:
                    print("          -----*-*-*-*-*-----          ")
                    print("ALL THE CHANGES YOU HAVE MADE ARE SAVED")
                    print("---------------------------------------")
                    print("                                       ")


            if Choice==2:
                print("-----WELCOME ADMIN-----")
                print("----------------------- \n")
                data=c1.fetchall()
                a=input("Enter The EmpID of the employee whom u want to delete the Details of:- \n")
                ea="DELETE FROM emp WHERE EmpID =".format(a)
                c1.execute(ea)
                con.commit()
                print("_______________________________")
                print("------DELETED SUCCESSFULLY-----")
                print("_______________________________")


            if Choice==3:
                EmpID=int(input("Enter The EmpID of the Employee You Want To see Details Of:-"))
                c1.execute("Select*from emp WHERE EmpID="+str(EmpID) )
                data=c1.fetchall()
                for row in data:
                    print("-----------------------------------")
                    print("---------Employee Details---------")
                    print("EmpID:-", EmpID)
                    print("FullName:-", row[1])
                    print("Age:-", row[2])
                    print("Gender:-", row[3])
                    print("Desgination:-", row[4])
                    print("salary", row[5])
                    print("Email:-", row[6])
                    print("Dob:-", row[7])
                    print("-------Employee Details Loaded-------")
                    print("------------------------------------- \n")
"""