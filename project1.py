def txtsp(a):
    import pyttsx3
    ts = pyttsx3.init()
    ts.say(a)
    print(a)
    ts.runAndWait()

def getdate():
    import datetime
    return datetime.datetime.now()
    
txtsp("Enter Your Name:")
na = input()

def wishme():
    hour = getdate().hour
    # print(hour)
    if hour >= 0 and hour < 12:
        txtsp(f"Hello {na} Good Morning!")
    elif hour >= 12 and hour < 16:
        txtsp(f"Hello {na} Good Afternoon!")
    else:
        txtsp(f"Hello {na},Good Evening!")
wishme()

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",database="kdiet")

mycursor = mydb.cursor()

def log1():
    txtsp(f"{na},Please Enter Name Of Food You Eatten:")
    f1 = input()
    s="INSERT INTO allclient (food,datentime,name) VALUES (%s,%s,%s)"
    date = getdate()
    value = (f1,date,na)
    mycursor.execute(s,value)
    mydb.commit()
    txtsp(f"{na}Your Diet is Successfully Updated")
    txtsp("Thank You")
    
def retrive():
    q = "SELECT * FROM allclient WHERE name = %s"
    name = (na,)
    mycursor.execute(q,name)
    records = mycursor.fetchall()
    for i in records:
        print(i)
        
txtsp(f"{na},Enter l For Log r For Retrive-")
uc = input()
if uc == "l":
    log1()
elif uc == "r":
    retrive()
else:
    txtsp("Enter Valid Data")

