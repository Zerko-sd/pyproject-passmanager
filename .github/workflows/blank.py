import mysql.connector as mys
import string
import random
import datetime
from dateutil.relativedelta import relativedelta
import tkinter
from tkinter import messagebox
from tkinter import *



mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'Nitish@1006', database = 'pwd_manager')
mycur = mycon.cursor()



def generate():
    passw = ''
    symbols = string.punctuation
    lst_symbols = []
    lst_numb = []
    lst_aplUP = []
    lst_aplLO = []
    for i in range(65,92):
        lst_aplUP.append(chr(i))
    for i in range(0,10):
        lst_numb.append(str(i))
    for i in symbols:
        lst_symbols.append(i)
    for i in range(65,92):
        lst_aplLO.append(chr(i).lower())
    while len(passw) < 13:
        choi = random.randint(1,4)
        if choi == 1:
            i = random.randint(0,len(lst_aplUP)-1)
            input_thing = lst_aplUP[i]
            passw += input_thing
        elif choi == 2:
            j = random.randint(0,len(lst_numb)-1)
            input_thing = lst_numb[j]
            passw += input_thing
        elif choi == 3:
            k = random.randint(0,len(lst_symbols)-1)
            input_thing = lst_symbols[k]
            passw += input_thing
        elif choi == 4:
            l = random.randint(0,len(lst_aplLO)-1)
            input_thing = lst_aplLO[l]
            passw += input_thing
    return passw


def create():
    mycur.execute("create table Manager(PassID int primary key, Website_URL varchar(50), Username varchar(20), Password varchar(20));")
    mycon.commit()

def insert(p):
    a = input("Enter Website URL: ")
    b = input("Enter Username: ")
    t = int(input('''Enter 0 to choose own password!
Enter 1 to generate strong password: '''))
    if t == 0:
        c = input("Enter Password: ")
    elif t == 1:
        c = generate()
    mycur.execute("insert into Manager values('%s','%s','%s','%s');"%(p,a,b,c))
    ######################
    x = datetime.datetime.now()
    result = x + relativedelta(months=+1)
    
    mycur.execute("insert into exp values('%s','%s','%s','%s')"%(p,b,c,str(result)))  #-------------
    mycon.commit()
    ##############################
    mycon.commit()
    print("Insertion complete!")
def display():
    mycur.execute("SELECT * FROM Manager")
    result = mycur.fetchall()
    print("PASSID\t\tWebsite_URL\t\t Username\t\tPassword")
    for row in result:
        passw = row[0]
        a = row[1]
        b = row[2]
        c = row[3]
        i = j = k = 1
        while True:
            if i == 23 or j == 20 or k == 14:
                break
            else:
                if len(a) == i:
                    p1 = ""
                    for p in range(22-i):
                        p1 = p1 + " "
                    p1 = p1 + " "
                if len(b) == j:
                    p2 = ""
                    for p in range(21-j):
                        p2 = p2 + " "
                    
                if len(str(passw)) == k:
                    p3 = ""
                    for p in range(14-k):
                        p3 = p3 + " "

            i = i + 1
            j = j + 1
            k = k + 1

        print(passw,p3,a,p1,b,p2,c)
    print()
def display_exp():
    mycur.execute("Select * from exp")
    result = mycur.fetchall()
    print("PASSID\t\tUsername\t\tPassword\t\tExpiry_Date")
    for row in result:
        a = row[0]
        b = row[1]
        c = row[2]
        d = row[3]
        i = j = k = 1
        while True:
            if i == 14 or j == 20 or k == 20:
                break
            else:
                if len(str(a)) == i:
                    p1 = ""
                    for p in range(13-i):
                        p1 = p1 + " "
                    p1 = p1 + " "
                if len(b) == j:
                    p2 = " "
                    for p in range(21-j):
                        p2 = p2 + " "
                    
                if len(str(c)) == k:
                    p3 = " "
                    for p in range(21-k):
                        p3 = p3 + " "
            i = i + 1
            j = j + 1
            k = k + 1
        print(a,p1,b,p2,c,p3,d)
    print()
def passid_():
    mycur.execute("select * from Manager;")
    d = mycur.fetchall()
    print(d)
    ap = len(d)

    if ap != 0:
        passid = ap
        return passid
    elif ap == 0:
        passid = 0
        return passid
def loopin(a):
    n = int(input("N: "))
    for i in range(n):
        a = a + 1
        b = str(a)
        insert(b)

def imp_exp():
    mycur.execute("Select * from manager")
   
        
    
#-------------------------------------------------------------------------------------------------------------------------------------
# Function Calls:

#create()a = passid_()loopin(a)
#display()
#mycur.execute("drop table Manager;")mycon.commit()
p = passid_()
insert(p)




    
