
import sqlite3
import datetime
import numpy as np
import pandas as pd

conn = sqlite3.connect("Employee.db")
c = conn.cursor()
conn.commit()

def employee_table():
    c.execute("CREATE TABLE IF NOT EXISTS Employee(ID INTEGER PRIMARY KEY,"
              "EmployeeID TEXT,StartDate TEXT,Seniority TEXT)")

employee_table()

        
def Creat_table_fenx_employee():
    c.execute("CREATE TABLE IF NOT EXISTS fenix_redeemed_points(id PRIMARY KEY,employee_id INTEGER,redeem INTEGER,approved TEXT)")

Creat_table_fenx_employee()
        

accural = {'A':5,'B':10,'C':15,'D':20,'E':25}
tenure = {'one_two':1,'two_four':1.25,'four_plus':1.5}

def insert_employee(empid,startdate,seniority):
    c.execute("INSERT INTO Employee (EmployeeID,StartDate,Seniority) VALUES(?,?,?)",(empid,startdate,seniority))
    conn.commit()

def queary_points(empid):
    start = []
    sen = []
    datelist = []
    year = []
    
    c.execute("SELECT * FROM Employee WHERE EmployeeID = ?",(empid,))

    for row in c.fetchall():
        
        startdate = row[2]
        seniority = row[3]

        start.append(startdate)
        sen.append(seniority)

    count = 0
    count1 = 0
    count2=0
    while count<len(start):
        date = datetime.datetime.strptime(start[count],"%Y/%m/%d")
        period = datetime.datetime.today().year-date.year
        datelist.append(period)
        year.append(date.year)
        count+=1

    v=[]
    while count2<len(year):
        if count2<len(year)-1 :
            if start[count2]> start[count2+1]:
                 dtr = pd.date_range(start=start[count2+1], end=start[count2], freq="D")
                 delta2 = (dtr[-1].to_period('M') - dtr[0].to_period('M')).n
                 v.append(delta2)
                 count2+=1
            else:
                dtr = pd.date_range(start=start[count2], end=start[count2+1], freq="D")
                delta2 = (dtr[-1].to_period('M') - dtr[0].to_period('M')).n
                v.append(delta2)
                count2+=1                
        else:
            break
    print(v)
    while count1<len(year):
        x = datelist[count1]
        y = sen[count1]

        
        if count1<len(v)>0  :
        
            if x >= 1 & x <= 2:
                w = tenure.get('one_two')

                if y == 'A':
                    q = accural.get('A')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                elif y == 'B': 
                    q = accural.get('B')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                elif y == 'C':
                    q = accural.get('C')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')
                    
                elif y == 'D':
                    q = accural.get('D')
                    points = w*q*v[count1]
                    print('For '+str([count1])+' you have '+str(points)+ ' points')

                elif y == 'E':
                    q = accural.get('E')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                else:
                    print('Error')

            elif x >= 2 & x <= 4:
                w = tenure.get('two_four')

                if y == 'A' :
                    q = accural.get('A')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                elif y == 'B':
                    q = accural.get('B')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                elif y == 'C':
                    q = accural.get('C')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')
                    
                elif y == 'D':
                    q = accural.get('D')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                elif y == 'E':
                    q = accural.get('E')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                else:
                    print('Error')

            elif x > 4:
                w = tenure.get('four_plus')

                if y == 'A':
                    q = accural.get('A')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                elif y == 'B':
                    q = accural.get('B')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                elif y == 'C':
                    q = accural.get('C')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')
                    
                elif y == 'D':
                    q = accural.get('D')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                elif y == 'E':
                    q = accural.get('E')
                    points = w*q*v[count1]
                    print('For '+str(start[count1])+' you have '+str(points)+ ' points')

                else:
                    print('Error')

            else:
                print('Out of range')

            count1+=1

            
        else:
            break

def accessBenefit() :
        total_points = 0
        user_id = int(input("Enter employee id: "))
      
        c.execute("SELECT EmployeeID FROM Employee")
        result = c.fetchall()
        user = False
        
        for x in result:
            
            if user_id in result :
                    user = True

            if True:
                
                benefit = 0
                while benefit != 3 :
                    print("1. Check balance")
                    print("2. Redeem Benefit")
                    print("3. Exit")
                    benefit = int(input())

                    if benefit == 1 :
                        total_points = queary_points(user_id)
                        print('Available points ', total_points)
                        print("\n\n")
                    elif benefit == 2 :
                            
                        total_points = queary_points(user_id)
                        print('Available points ', total_points)
                        redeem = int(input("Redeem points: "))
                        manager = int(input("Enter Supervisor ID: "))
                        if redeem <= total_points :
                            approved=points-redeem
                            c.execute("INSERT INTO fenix_redeemed_points (redeem, employee_id, manager_id, approved) VALUES (?, ?, ?, ?)", (redeem, user_id, manager, 0))
                            conn.commit()
                            print("Requested")
                            
                            print("\n\n")
                        else:
                                    
                            print("Requested points less than available points")
                            print("\n\n")

                    elif benefit == 3 :
                    
                        break
                    else :
                            continue
            else :
                    print("User does not exist")
                    print("\n\n")
            




def approveBenefit():
        _id = int(input("Enter employee id: "))
        #mysql = db.cursor()
        c.execute("SELECT EmployeeID FROM Employee ")
        result = c.fetchall()
        employee = False
        for x in result:
            if _id in x:
                
                employee = True

        if employee :
            
            c.execute("SELECT id, employee_id, redeem FROM fenix_redeemed_points WHERE manager_id = ? AND approved = ?", (_id, 0),)

            result = c.fetchall()

            if len(result) > 0:
                    count = 1
                    _dict = dict()
                    for x in result:
                        print(str(x[0]) + ". Employee " + str(x[1]) + " wants to redeem " + str(x[2]) + " points")
                        _dict[str(x[0])] = x[0]
                        if count == len(result):
                                print("Select redeem number to redeem points: ")

                        count = count + 1

                    approve = input()
                    if approve in _dict :
                        c.execute("UPDATE fenix_redeemed_points SET approved = 1 WHERE id = ?", (int(approve), ))
                        conn.commit()

                    else :
                            print("Not requests for points to be redeemed")
                            print("\n\n")
            else :
                    print("User Id does not exist")
                    print("\n\n")
'''
 f
'''
def program():
    


    x = int(input("Enter \n 1 to insert Employee \n 2 to queary employee points \n 3 access benefits \n 4 approve benefits: "))

    if x == 1:
        while True:
            y = input("Employee ID: ")
            z = input("Start Date: ")
            a = input("Seniority: ")

            insert_employee(y,z,a)

            if y or z or a == 'Exit':
                break
                program()

    elif x == 2:
        y = input("Employee ID: ")
        queary_points(y)

    elif x==3:
        accessBenefit()

    elif x==4:
        approveBenefit()      

    else:
        print('Enter either 1 or 2')
        program()

program()

  

        
        


    
