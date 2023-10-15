import mysql.connector as mys
import string
import random
import datetime
from dateutil.relativedelta import relativedelta
from tabulate import tabulate

MKEY = "xyz"                                                                  #For now, I assumed value for Master key



mycon = mys.connect(host = 'localhost', user = 'root', passwd = '0408', database = 'pwd_manager')
mycur = mycon.cursor()
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
    return passw

def create():
    mycur.execute("create table Manager(PassID int primary key, Website_URL varchar(50), Username varchar(20), Password varchar(20));")
    mycur.execute("create table exp(passid_ int primary key, username varchar(30), password varchar(20), exp_date date);")
    mycon.commit()

def insert(p):                                                                          # Loop for insert begins with loopin(passid_()) function
    a = input("Enter Website URL: ")
    b = input("Enter Username: ")
    t = int(input('''Enter 0 to choose own password!
Enter 1 to generate strong password: '''))
    if t == 0:
        c = input("Enter Password: ")
    elif t == 1:
        c = generate()
    mycur.execute("insert into Manager values(%s,'%s','%s','%s');"%(p,a,b,c))

    x = datetime.datetime.now()
    result = x + relativedelta(months=+1)

    mycur.execute("insert into exp values(%s,'%s','%s','%s')"%(p,b,c,str(result)))
    mycon.commit()

    print("Insertion complete!")

def display():
    x = input("Enter Master Key: ")
    if x == MKEY:
        mycur.execute("SELECT * FROM Manager")
        result = list(mycur.fetchall())
        print(tabulate(result, headers=['Password ID', 'Website URL', 'Username','Password'], tablefmt='fancy_outline'))
    else:
        print("Incorrect Master key")
def display_exp():
    x = input("Enter Master Key: ")
    if x == MKEY:
        mycur.execute("Select * from exp")
        result = mycur.fetchall()
        print(tabulate(result, headers=['Password ID', 'Username', 'Password','Expiry Date'], tablefmt='fancy_outline'))
    else:
        print("Incorrect Master key")

def delete():
    auth = input("Enter Master key: ")
    if auth == MKEY:
        rurl, ruser = input("Enter URL and Username of password to be retrieved: ")
        mycur.execute("select * from Manger;")
        d = mycur.fetchall()
        for i in d:
            if i[1] == rurl and i[2] = ruser:
                p = i[0]
        mycur.execute("delete from Manager where PassID=%s;"%(p,))
        mycur.execute("delete from exp where passid=%s;"%(p,))
        mycon.commit()
    
def exp_delete():
    x = datetime.date.today()
    mycur.execute("select * from exp;")
    t = mycur.fetchall()
    for i in t:
        if i[3] == x:
            p = i[0]
            mycur.execute('delete from Manager where PassID=%s;'%(p,))
            mycur.execute('delete from exp where passid_=%s;'%(p,))
            mycon.commit()
        else:
            continue


def retrieve():
    auth = input("Enter Master key: ")
    if auth == MKEY:
        rurl, ruser = input("Enter URL and Username of password to be retrieved: ")
        mycur.execute("select Password from Manager where Username='%s' and Website_URL = '%s';"%(ruser,rurl))
        pswd = mycur.fetchone()
        print("Desired Password: ", pswd)
    else:
        print("Incorrect Master Key")
    
def passid_():                                               # Checks for latest password ID and returns value for loopin() function
    mycur.execute("select * from Manager;")
    d = mycur.fetchall()
    ap = len(d)
    if ap != 0:
        passid = ap
        return passid
    elif ap == 0:
        passid = 0
        return passid
def loopin(a):                                               # Takes arg from passid_() and starts inserting record using insert()
    n = int(input("N: "))
    for i in range(n):
        a = a + 1
        b = str(a)
        insert(b)


#___________________________________________________________________________________________
# Function Calls:



    
