import mysql.connector
import base64
import os
import hashlib
import subprocess
import time
import sys
import requests
from time import sleep
from colorama import Fore, Back, Style
#check hardware id
def get_serialnumber():
    return subprocess.check_output("wmic bios get serialnumber", shell=True).decode().split('\n')[1].strip()
def get_hardwareid():
    return subprocess.check_output("wmic csproduct get uuid", shell=True).decode().split('\n')[1].strip()
def get_ip():
    return requests.get('https://api.ipify.org').text
waiting = Fore.CYAN+"["+Fore.LIGHTMAGENTA_EX+"#"+Fore.CYAN+"]"+Fore.RESET
succes = Fore.CYAN+"["+Fore.LIGHTGREEN_EX+"+"+Fore.CYAN+"]"+Fore.RESET
error = Fore.CYAN+"["+Fore.LIGHTRED_EX+"-"+Fore.CYAN+"]"+Fore.RESET
warning = Fore.CYAN+"["+Fore.LIGHTYELLOW_EX+"!"+Fore.CYAN+"]"+Fore.RESET
inputpre = Fore.CYAN+"["+Fore.GREEN+"$"+Fore.CYAN+"]"+Fore.RESET+"|>>>"
found_pre = Fore.LIGHTCYAN_EX+"["+Fore.LIGHTMAGENTA_EX+"#"+Fore.LIGHTCYAN_EX+"]"+Fore.RESET+" "
os.system("title STKnetworx")

print(waiting+" Connecting to STKnetworx...")
mydb = mysql.connector.connect(
    host="87.118.122.106",
    user="consi_db2",
    passwd=base64.b64decode("SG11eG4hOFc5OSVZ").decode("utf-8"),
    database="consi_db2"
)
os.system("title STKnetworx")
mycursor = mydb.cursor()

def checkinternet():
    try:
        requests.get('https://www.google.com')
        return True
    except requests.ConnectionError:
        return False
def lastlog ():
    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")
    timec = time.strftime("%H:%M:%S")
    string = f"{day}/{month}/{year} {timec}"
    return string

def main(user):
    while True:
        msg = input(inputpre+f" {user} > ")
        if msg.startswith("/"):
            if user == "stk": #admin
                cmd = msg[1:]
                if cmd == "clear":
                    mycursor.execute("DELETE FROM messages")
                    mydb.commit()
                    print(succes+" Database cleared!")

        
        else:
            mycursor.execute("INSERT INTO messages (user, message) VALUES (%s, %s)", (user, msg))
            mydb.commit()


def login():
    os.system("cls")
    username = input(inputpre+" Username: ")
    password = input(inputpre+" Password: ")
    password = hashlib.sha256(password.encode()).hexdigest()
    mycursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        print(error+" Wrong username or password!")
        sleep(1)
        login()
    else:
        mycursor.execute("UPDATE user SET lastlog = %s WHERE username = %s", (lastlog(), username))
        mydb.commit()
        print(succes+" Logged in!")
        sleep(1)
        print("Starting STKnetworx manager...")
        os.system(f"start C:\\STK\\bin\\STK\\asset\\stknetmsg.py {username}")
        os.system("cls")
        print(succes+" Welcome back, "+username+"!")
        os.system(f"title STKnetworx - {username}")
        main(username)
devmode = False
def start():
    if checkinternet():
        if mydb.is_connected():
            print(succes+" Connected to STKnetworx!")
            if devmode:
                print("Loading data")
                print (get_serialnumber())
                print (get_hardwareid())
                print (get_ip())
            mycursor.execute("SELECT * FROM user WHERE hwid = %s", (get_hardwareid(),))
            myresult = mycursor.fetchall()
            if devmode:
                print (myresult)
            if len(myresult) == 0:
                print(error+" No account found!")
                print(warning+" Please register an account first! Enter to continue...")
                input()
                os.system("cls")
                print(inputpre+" Register an account")
                username = input(inputpre+" Username: ")
                mycursor.execute("SELECT * FROM user WHERE username = %s", (username,))
                myresult = mycursor.fetchall()
                if not len(myresult) == 0:
                    print(error+" Username already taken!")
                    print(warning+" Please try another username! Enter to continue...")
                    input()
                    os.system("cls")
                    start()
                password = input(inputpre+" Password: ")
                password = hashlib.sha256(password.encode()).hexdigest()
                mycursor.execute("INSERT INTO user (`biosnr`, `username`, `password`,`hwid`,`ip`) VALUES (%s, %s, %s, %s, %s)", (get_serialnumber(), username, password, get_hardwareid() ,get_ip()))
                mydb.commit()
                print(succes+" Account registered!")
                print(warning+" Press enter to continue...")
                input()
                os.system("cls")
                login()
            else:
                print(succes+" Account found!")
                os.system("cls")
                login()

        else:
            print(error+" Failed to connect to STKnetworx!")
            exit()
    else:
        print(error+" No internet connection!")
        exit()
start()