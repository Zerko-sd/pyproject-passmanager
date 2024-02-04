import mysql.connector as mys
import string
import random
import datetime
from dateutil.relativedelta import relativedelta
import os
import time
from tabulate import tabulate
import pyperclip


mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'Nitish@1006', database = 'pwd_manager')
mycur = mycon.cursor()
MKEY = "XYZ"       


def generate():
    passw = ''
    symbols = string.punctuation
    symbols = list(symbols.partition(" "))
    symbols.pop(1)
    symbols = symbols[0] + symbols[1]
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
    pyperclip.copy(passw)
    return passw


def create():
    mycur.execute("create table Manager(PassID int primary key, Website_URL varchar(50), Username varchar(20), Password varchar(20));")
    mycur.execute("create table exp(passid_ int primary key, username varchar(30), password varchar(20), exp_date date);")
    mycon.commit()

def insert(p):
    print(30*"-","Insertion",30*"-")
    a = input("Enter Website URL: ")
    b = input("Enter Username: ")
    t = int(input('''Enter 0 to Enter own password!
Enter 1 to generate strong password: '''))
    if t == 0:
        c = input("Enter Password: ")
        print("Password addition/updation done!")
        print("Exiting now")
        time.sleep(3)
    elif t == 1:
        c = generate()
        print("The password has been copied to clipboard!")
        print(c)

        print("Password addition/updation done!")
        print("Exiting now")
        time.sleep(4)
        
    ######################
    mycur.execute("insert into manager values(%s,'%s','%s','%s')"%(p,a,b,c))
    mycur.execute("insert into dummy values(%s,'%s','%s','%s')"%(p,a,b,c))
    mycon.commit()
    ######################
    x = datetime.datetime.now()
    result = x + relativedelta(months=+1)
    log = open("C:\\Users\\schit\\Downloads\\activity_log\\"+str(p)+".txt","a+")
    upd = [a,b,"Changed to "+c,"At The Date And Time:",datetime.datetime.now()]
    log.write(str(upd))
    log.close()

    mycur.execute("insert into exp values(%s,'%s','%s','%s')"%(p,b,c,str(result)))  #-------------
    mycon.commit()
    ##############################
    print("Insertion complete!")
    os.system('cls')
def display():
    x = input("Enter Master Key: ")
    if x == MKEY:
        print(30*"-","Displaying",30*"-")
        mycur.execute("SELECT * FROM manager")
        result = list(mycur.fetchall())
        print(tabulate(result, headers=['Password ID', 'Website URL', 'Username','Password'], tablefmt='fancy_outline'))
    else:
        print("Incorrect Master key")

def passid_():
    mycur.execute("select * from dummy;")
    d = mycur.fetchall()
    ap = len(d)

    if ap != 0:
        passid = ap
        return passid
    elif ap == 0:
        passid = 0
        return passid

def delete():
    print(30*"-","Deletion",30*"-")
    p = passid_()
    auth = input("Enter Master key: ")
    if auth == MKEY:
        rurl = input("Enter URL of password to be deleted: ")
        ruser = input("Enter Username of password to be deleted: ")
        mycur.execute("select * from manager;")
        d = mycur.fetchall()
        for i in d:
            if i[1] == rurl and i[2] == ruser:
                p = i[0]
        mycur.execute("delete from manager where PassID=%s;"%(p,))
        mycur.execute("delete from exp where passid_=%s;"%(p,))
        mycon.commit()
        print("Process Done!")
        time.sleep(3)



def retrieve():
    print(30*"-","Retrieve",30*"-")
    auth = input("Enter Master key: ")
    if auth == MKEY:
        rurl = input("Enter URL of password to be retrieved: ")
        ruser = input("Enter Username of password to be retrieved: ")
        mycur.execute("select Password from manager where Username='%s' and Website_URL = '%s';"%(ruser,rurl))
        pswd = mycur.fetchone()
        print("Desired Password: ", pswd)
    else:
        print("Incorrect Master Key")


def export():
    print(30*"-","Export",30*"-")
    mycur.execute("Select * from manager")
    main = mycur.fetchall()
    a = open("C:\\Users\\schit\\Downloads\\export.txt","w+")
    for i in main:
        a.write(str(i)+"\n")
    a.close()

def upd():
    print(30*"-","Updating",30*"-")
    auth = input("Enter Master key: ")
    if auth == MKEY:
        rID = input("Enter PassID of password to be updated: ")
        mycur.execute("delete from manager where PassID = %s;"%(rID,))
        mycon.commit()
        print("wait a moment...")
        time.sleep(3)
        p = passid_()
        insert(p)
        print("Completed updation!")
    else:
        print("Incorrect Master Key")


    
#-------------------------------------------------------------------------------------------------------------------------------------


'''-------------------main--------------------'''

flag = True
while flag == True:
    os.system('cls')
    print(15*'~'+'  Password Manager  '+15*'~')
    print()
    username = input("Enter Your Username: ")
    if username == "Nitish123":
        os.system('cls')
        print(15*'~'+'  Password Manager  '+15*'~')
        print()
        print("Username :"+username)
        print()
        passwrd = input("Enter Your Password: ")
        if passwrd == "Admin":
            print("Access Granted...Welcome Back!")
            time.sleep(3)
            os.system('cls')
            print(15*"-","   Menu   ",15*'-')
            print()
            print("1.Add New Account")
            print("2.Delete Existing Account")
            print("3.Updation of records")
            print("4.View All Saved Data")
            print("5.Retrieve Passwords")
            print("6.Exporting Passwords")
            print("7.exit")
            inpp = int(input(":"))
            
            if inpp == 1:
                os.system('cls')
                p = passid_()
                insert(p)
                umm = input("Press any key to exit...")
                os.system('cls')  
                # add the account thing function
            elif inpp == 2:
                os.system('cls')
                delete()
                exp_delete()
                umm = input("Press any key to exit...")
                os.system('cls')
                print()
                    
                # delete the account thing function
            elif inpp == 3:
                os.system('cls')
                upd()
                umm = input("Press any key to exit...")
                print()
                # update info of an account
            elif inpp == 4:
                os.system('cls')
                display()
                dumm = input("Press any key to exit...")
                os.system('cls')
                print()
                # view all saved data    
            elif inpp == 5:
                os.system('cls')
                retrieve()
                dumm = input("Press any key to exit...")
            
            elif inpp == 6:
                os.system('cls')
                print("Password Exporting in progress....")
                export()
                time.sleep(3)
                print("Process Done!")
                time.sleep(3)

            elif inpp == 7:
                os.system('cls')
                umm = input("Press any key to exit...")
                exit()
        else:
            os.system('cls')
            break
