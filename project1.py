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
    q = "SELECT food,datentime FROM allclient WHERE name = %s"
    name = (na,)
    mycursor.execute(q,name)
    records = mycursor.fetchall()
    for i in records:
        print(i)
        
def result():
    junk = ("Pizza", "Burger", "Sweets")

    q1 = "SELECT COUNT(srno) FROM allclient WHERE name = %s and (food = %s OR food = %s OR food = %s)"
    val = (na, junk[0], junk[1], junk[2])
    mycursor.execute(q1, val)
    records = mycursor.fetchall()
    q2 = "SELECT COUNT(srno) FROM allclient WHERE name = %s and food != %s AND food != %s AND food != %s"
    val1 = (na, junk[0], junk[1], junk[2])
    mycursor.execute(q2, val1)
    records1 = mycursor.fetchall()
    for j in records:
        junkf = int(j[0])
        # print(junkf)
    for h in records1:
        healthyf = int(h[0])
        # print(healthyf)

    if healthyf > junkf:
        txtsp("Your Diet Is Going Well, Keep Going")
    else:
        txtsp("OOh! , Please Start Eating Healthy")

    txtsp("These is Your Result")
    from matplotlib import pyplot as plt
    l1 = [junkf, healthyf]
    l2 = ["Junk","Healthy"]
    plt.pie(l1,labels = l2 ,autopct='%1.2f%%')
    plt.legend()
    plt.show()



txtsp(f"{na},Enter L For Log R For Retrive S Show Results")
uc = input()

if uc.capitalize() == "L":
    log1()
elif uc.capitalize() == "R":
    retrive()
elif uc.capitalize() == "S":
    result()
else:
    txtsp("Enter Valid Data")

