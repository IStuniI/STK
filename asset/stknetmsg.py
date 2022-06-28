import mysql.connector
import base64
import os
import subprocess
import sys
import requests
from time import sleep
import time
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
user = sys.argv[1]
os.system("mode con cols=50 lines=25")
os.system(f"title STKnetworx - {user}")
print(waiting+" Connecting to STKnetworx...")
mydb = mysql.connector.connect(
    host="87.118.122.106",
    user="consi_db2",
    passwd=base64.b64decode("SG11eG4hOFc5OSVZ").decode("utf-8"),
    database="consi_db2"
)

cursor = mydb.cursor()
if mydb.is_connected():
    print(succes+" Connected to STKnetworx!")
    print("Loading data")
    print (get_serialnumber())
    os.system("cls")
    print (get_hardwareid())
    os.system("cls")
    print (get_ip())
    os.system("cls")
    while True:
        mydb = mysql.connector.connect(
        host="87.118.122.106",
        user="consi_db2",
        passwd=base64.b64decode("SG11eG4hOFc5OSVZ").decode("utf-8"),
        database="consi_db2"
        )
        cursor = mydb.cursor()
        os.system("cls")
        cursor.execute("SELECT * FROM messages ORDER BY id DESC")
        messages = cursor.fetchall()
        for message in messages:
            if message[1] == user:
                print(found_pre+Fore.LIGHTYELLOW_EX+f" {message[1]}"+Fore.CYAN+"> "+Fore.LIGHTRED_EX+f"{message[2]}")
            else:
               print(found_pre+f" {message[1]}> {message[2]}")
        sleep(1)


else:
    print(error+" Failed to connect to STKnetworx!")
    exit()