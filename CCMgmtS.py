import mysql.connector as mycon
import csv
from csv import writer

con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
if con.is_connected():
    print("---------")
    print("Connected")
    print("---------")
    c1 = con.cursor()
    c1.execute("show databases;")
    data=c1.fetchall()
    print(data)
    
    if("ccmgmts",) in data:
        print("Database Exists")
        c1.execute("use ccmgmts")
    else:
        c1.execute("create database ccmgmts")
        print("Database Created")
        c1.execute("use ccmgmts")

else:
    print("----------------")
    print("")
    print("Connection Failed. \n")
    print("")
    print("PLEASE TRY AGAIN.")


def about():
    f=open('about.txt','r')
    content = f.read()
    print(content)


def new_customer():
    
    Customer_Name = input("Enter Your Name:-")
    Phone_no = int(input("Enter Your Phone Number:-"))
    Email = input("Enter Your Email ID:-")
    abc = "INSERT INTO new_customer (Customer_Name, Phone_no, Email) VALUES ('{}', '{}', '{}')".format(Customer_Name, Phone_no, Email)
    c1.execute(abc)
    con.commit()
    print("")
    print("-----   THANK YOU FOR VISITING   -----")
    print("")
    print("----- Hope You Have A Great Time -----")
    print("")


def Customer_Bill():

    f = open("bill.csv", 'a')
    writer = csv.writer(f)
    
    Customer_Name = input("Enter Your Name:-")
    Accessed_Time = int(input("Enter the time you have accessed our cyber cafe in minutes:-"))
    Total_Bill = Accessed_Time * 5
    
    writer.writerow([Customer_Name, Accessed_Time, Total_Bill])
    f.close()
    
    yz = "INSERT INTO Bill (Customer_Name, Accessed_Time, Total_Bill) VALUES ('{}', '{}', '{}')".format(Customer_Name,Accessed_Time,Total_Bill)
    c1.execute(yz)
    con.commit()
    print("")
    print("Please Pay Rs.", Total_Bill)
    b = input("Type Yes or No") 
    
    if b == "Yes":
        print("                *Your Bill has been paid successfully*")
        print("                 ------------------------------------                 ")
        print("  Thank You for visiting to City Cyber Cafe We Wish to serve you again")
        print("")
    else:
        print("")
        print("#___________________________________________________#")
        print("Bill not Paid, Kindly Pay the bill to leave the cafe.")
        print("#___________________________________________________#")
        print("")


def Employee():
    
    con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
    c1 = con.cursor()
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

            con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
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
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                elif Choice==2:
                    data=c1.fetchall()
                    a=input("Enter Age:-")
                    b=input("Enter EmpID:-")
                    st="UPDATE emp Set Age = '{}' where EmpID = '{}'".format(a,b)

                    c1.execute(st)
                    con.commit()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                elif Choice==3:
                    data=c1.fetchall()
                    a=input("Enter Designation:-")
                    b=input("Enter EmpID:-")
                    st="UPDATE emp Set Designation = '{}' where EmpID = '{}'".format(a,b)

                    c1.execute(st)
                    con.commit()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                elif Choice==4:
                    data=c1.fetchall()
                    a=input("Enter Salary:-")
                    b=input("Enter EmpID:-")
                    st="UPDATE emp Set Salary = '{}' where EmpID = '{}'".format(a,b)

                    c1.execute(st)
                    con.commit()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                elif Choice==5:
                    data=c1.fetchall()
                    a=input("Enter Email:-")
                    b=input("Enter EmpID:-")
                    st="UPDATE emp Set Email = '{}' where EmpId = '{}'".format(a,b)

                    c1.execute(st)
                    con.commit()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                elif Choice==6:
                    print("          -----*-*-*-*-*-----          ")
                    print("ALL THE CHANGES YOU HAVE MADE ARE SAVED")
                    print("---------------------------------------")
                    print("                                       ")


        elif Choice==2:
            print("-----WELCOME ADMIN-----")
            print("----------------------- \n")

            #c1 = con.cursor()
            #data=c1.fetchall()
            a=input("Enter The EmpID of the employee whom u want to delete the Details of:- \n")
            ea="DELETE FROM emp WHERE EmpID ={}".format(a)
            c1.execute(ea)
            con.commit()
            print("_______________________________")
            print("------DELETED SUCCESSFULLY-----")
            print("_______________________________")


        elif Choice==3:
            c1 = con.cursor()
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

        elif Choice==4:
            print("")
            print("Thank You Admin.")
            print("")        



def Cutomer_Details():
    
    con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
    c1 = con.cursor()
    username = input("Enter Your Username(Admins Only):-")
    password = input("Enter Your Password(Admins Only):-")
    usname = 'ccmgmts'
    passwd = 'cafe'


    if (username == usname) and (password == passwd):
        print("-----WELCOME ADMIN-----")
        print("1.Update Customer Details.")
        print("2.View Customer Details.")
        print("3.Exit.")
        
        Choice = int(input("Enter Your Choice:-"))
        
        if Choice==1:
            print("Choose What Detail You Want To Update:- /n")
            print("1.Customer_Name.")
            print("2.Email.")
            print("3.Exit.")
            
            Choice = int(input("Enter Your Choice:-"))
            
            con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
            
            if con.is_connected():
                print("Connection Success")
                c1 = con.cursor()
                c1.execute("Select * from new_customer")
                
                if Choice==1:
                    data=c1.fetchall()
                    a=input("Enter Your Name:- \n")
                    b=input("Enter Your Phone_no:- \n")
                    st = "UPDATE new_customer Set Customer_Name = '{}' where Phone_no = '{}'".format(a, b)
                    c1.execute(st)
                    con.commit()
                    print("*-----* SUCCESSFULLY UPDATED*-----* \n")

                elif Choice==2:
                    data=c1.fetchall()
                    a=input("Enter Your Email ID:- \n")
                    b=input("Enter Your Phone_no:- \n")
                    st = "UPDATE new_customer Set Customer_Name = '{}' where Phone_no = '{}'".format(a, b)
                    c1.execute(st)
                    con.commit()
                    print("*-----* SUCCESSFULLY UPDATED*-----*")

                elif Choice==3:
                    print("  *****-----*****--**--*****-----*****  ")
                    print("---------------THANK YOU----------------")
                    print("ALL THE CHANGES YOU HAVE MADE ARE SAVED.")
                    print("  *****-----*****--**--*****-----*****  ")


        elif Choice==2:
            Phone_no=int(input("Enter The Phon_no of the Customer You Want To see Details Of:-"))
            c1.execute("Select*from new_customer WHERE Phone_no="+str(Phone_no) )
            data=c1.fetchall()
            for row in data:
                print("-----------------------------------")
                print("-#-----#-Customer Details-#-----#-")
                print("Name:", row[1])
                print("Phone_no", row[2])
                print("Email", row[3])
                print("--$--Customer Details Loaded--$--")
                print("-----------------------------------")


        elif Choice==3:
            print("---------------")
            print("THANK YOU ADMIN")
            print("---------------")

        else:
            print("-------------------------------------------")
            print(" - - - I N V A L I D - - - I N P U T - - - ")
            print("-------------------------------------------")


def bill_stuff():
    Na=int(input("Enter You Choice:- \n"))
    
    if Na == 1:
        Customer_Bill()

    elif Na == 2:
        con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
        c1 = con.cursor()
        a=(input("Enter the Name Of Customer Whom You Want to Delete The Bill Of:- \n"))
        ea="DELETE from bill WHERE Customer_Name = '{}'".format(a)

        c1.execute(ea)
        data=c1.fetchall()
        con.commit()
        print("")
        print("*-----* Deleted Successfully*-----*")
        print("")

    elif Na == 3:
        print("")
        print("1.All Bills. \n")
        print("2.A Particular Bill. \n")
        print("3.Exit. \n")
        print("")

        ez=int(input("Enter You Choice:- \n"))

        if ez == 1:
            print("")
            print("-----HERE YOU GO-----")
            with open("bill.csv", "r") as bfh:
                billreader = csv.reader(bfh, delimiter = '|')
                for bill in billreader:
                    print(bill)

        elif ez == 2:
            print("")
            print("-----HERE YOU GO----- \n")
            Name=input("Enter The Name Of Customer You Want To See The Bill Of:- \n")
            f = open("bill.csv","r")
            for line in f:
                if Name in line:
                    print(line)

        elif ez == 3:
            print("")
            print("SAVED")
            print("")

        else:
            print("-------------------------------------------")
            print(" - - - I N V A L I D - - - I N P U T - - - ")
            print("-------------------------------------------")

    elif Na == 4:
        print("")
        print("-----THANK YOU-----")
        print("")

    else:
        print("-------------------------------------------")
        print(" - - - I N V A L I D - - - I N P U T - - - ")
        print("-------------------------------------------")

def new_employee():
    print("-----------------Hey-------------------")
    print("WE ARE LOOKING FORWARD TO WORK WITH YOU \n")
    print("")
    a = input("Enter Your EmpID:- \n")
    b = input("Enter Your FullName:- \n")
    c = input("Enter Your Age:- \n")
    d = input("Enter Your Gender:- \n")
    e = input("Enter Your Designation:- \n")
    f = input("Enter Your Salary:- \n")
    g = input("Enter Your EmailID:- \n")
    h = input("Enter Your DoB:- \n")
    ea = "INSERT INTO emp (EmpID, FullName, Age, Gender, Designation, salary, Email, DoB) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
        a, b, c, d, e, f, g, h)
    c1.execute(ea)
    con.commit()
    print("------------------------")
    print("THANK YOU FOR JOINING US")
    print("------------------------ \n")


while True:
    print("")
    print("|-----WELCOME TO CITY CYBER CAFE-----|")
    print()
    print("*-*City Cyber Cafe*-* \n")
    print("")
    print("1.Customer. \n")
    print("2.Bill. \n")
    print("3.Employee Details(ADMINS ONLY). \n")
    print("4.Customer Details. \n")
    print("5.New Employee. \n")
    print("6.About. \n")
    print("7.Cafe Usage. \n")
    print("8.Exit. \n")


    Choice = int(input("Enter Your Choice:- \n"))
    if Choice == 1:
        con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
        c1 = con.cursor()
        
        c1.execute("show tables;")
        data=c1.fetchall()
        print(data)
        
        if("new_customer",) in data:
            print("table Exists")
            new_customer()

        else:
            c1=con.cursor()
            c1.execute("create table New_Customer(ID int PRIMARY KEY NOT NULL AUTO_INCREMENT, Customer_Name varchar(25), Phone_no int(10) ,Email varchar(25))")
            con.commit()
            print("Table created")
            new_customer()


    elif Choice == 2:
        con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
        c1 = con.cursor()
        
        c1.execute("show tables;")
        data=c1.fetchall()
        print(data)

        if("bill",) in data:
            print("table Exists \n")
            print("")
            print("*------------------------*")
            print("WELCOME TO CITY CYBER CAFE")
            print("")
            print("1.Create New Bill. \n")
            print("2.Delete Bill. \n")
            print("3.View Bills. \n")1
            print("4.Exit. \n")
            print("")
            bill_stuff()
        else:
            c1=con.cursor()
            c1.execute("create Table Bill(Customer_Name varchar(20), Accessed_Time int, Total_Bill int)")
            con.commit()
            print("Table created")
            print("")
            print("*------------------------*")
            print("WELCOME TO CITY CYBER CAFE")
            print("")
            print("1.Create New Bill. \n")
            print("2.Delete Bill. \n")
            print("3.View Bills. \n")
            print("4.Exit. \n")
            print("")
            bill_stuff()
            

    elif Choice == 3:
        con=mycon.connect(host="localhost",password="Sudh2706",user="root",database="hi")
        c1 = con.cursor()
        c1.execute("show tables;")
        data=c1.fetchall()
        print(data)
        
        if("emp",) in data:
            print("Table Exists")
            print("")
            Employee()

        else:
            c1.execute("create table emp (EmpID VARCHAR(10), FullName VARCHAR(30), Age VARCHAR(10), Gender VARCHAR(10), Designation VARCHAR(15), Salary VARCHAR(10), Email VARCHAR(25), DoB DATE)")
            con.commit()
            print("table Created")
            print("")
            Employee()

        

    elif Choice == 4:
        Cutomer_Details()


    elif Choice == 5:
        if ("emp",) in data:
            print("Table Exists")
            print("")
            new_employee()

        else:
            c1.execute(
                "create table emp (EmpID VARCHAR(10), FullName VARCHAR(30), Age VARCHAR(10), Gender VARCHAR(10), Designation VARCHAR(15), Salary VARCHAR(10), Email VARCHAR(25), DoB DATE)")
            con.commit()
            print("table Created")
            print("")
            new_employee()


    elif Choice==6:
        about()

    
    elif Choice==7:
        import matplotlib.pyplot as mpt
        mem=[50,45,34,37,34,23,65]
        dayz=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        mpt.pie(mem, labels=dayz)
        mpt.show()

    
    elif Choice==8:
        print("")
        print("*------------------------------------------------------------------* \n")
        print("")
        print("----------------THANK YOU FOR VISITING CITY CYBER CAFE--------------- \n")
        print("")
        print("---------------------BYEEEEEEEEEEEEEEEEEEEEEEEE--------------------- \n")
        print("")
        print("*------------------------------------------------------------------* \n")
        break

    else:
        print("")
        print("-------------------------------------------------------------------------")
        print("")
        print(" ---------------------------- E R R O R ---------------------------------")
        print("")
        print("-------------------------------------------------------------------------")
        print("")
        print(" -P L E A S E --- E N T E R --- T H E --- C O R R E C T --- C H O I C E- ")
        print("")
        print("-------------------------------------------------------------------------")
        print("")



