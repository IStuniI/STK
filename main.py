import os
import base64
import sys
import requests
import shutil
 
#functions
def install_pkg(pkg):
    os.system("pip3 install " + pkg)

#VARS
author = "Stein#7722"
update_url = "https://raw.githubusercontent.com/IStuniI/STK/main/Bin/version.stk"
#BOOT
path = "C:\STK\\bin\STK"
packages = ["colorama"]
print("Installing")
#   install the packages
for pkg in packages:
    install_pkg(pkg)
    os.system("cls")
print(path)
os.system("cls")
version = open(path+"\\Bin\\version.stk", "r").read()


#other imports
try:
    import colorama
    from colorama import Fore, Style, Back
except:
    print("Cant install requirements!Please re install!")

#Prefix
waiting = Fore.CYAN+"["+Fore.LIGHTMAGENTA_EX+"#"+Fore.CYAN+"]"+Fore.RESET
succes = Fore.CYAN+"["+Fore.LIGHTGREEN_EX+"+"+Fore.CYAN+"]"+Fore.RESET
error = Fore.CYAN+"["+Fore.LIGHTRED_EX+"-"+Fore.CYAN+"]"+Fore.RESET
warning = Fore.CYAN+"["+Fore.LIGHTYELLOW_EX+"!"+Fore.CYAN+"]"+Fore.RESET
inputpre = Fore.CYAN+"["+Fore.GREEN+"$"+Fore.CYAN+"]"+Fore.RESET+"|>>>"


#built-in commands


def update():
    url = requests.get(update_url)
    if url.status_code == 200:
        os.system("cls")
        print(succes+" Checking for updates...")
        if version != url.text:
            print(succes+" Update found! New version: "+url.text + "You are running version: "+version)
            print("Do you want to update? (y/n)")
            cmd = input(inputpre+" ").lower()
            if cmd == "y":
                os.system("cls")
                print(succes+" Downloading...")
                os.system("git clone https://github.com/IStuniI/STK.git C:\STK\\bin\STKUP")
                os.system("cls")
                print(succes+" Downloaded! Cloning...")
                file_names = os.listdir("C:\STK\\bin\STKUP")
                for file_name in file_names:
                    #overwrite the old files
                    if file_name != "STK":
                        shutil.move("C:\STK\\bin\STKUP\\"+file_name, "C:\STK\\bin\\STK\\"+file_name)
                os.system("cls")
                print(succes+" Successfully updated! Restarting...")
                os.system(f"python3 {path}\\main.py")
            elif cmd == "n":
                print(succes+" Not updating...")
        else:
            print(succes+" No updates found!")
        
    else:
        print(error+" Update failed!")

def help():
    #try: 
    with open(path+"\\Bin\\help.stk", "rb") as f:
        lines = [x.decode('utf8').strip() for x in f.readlines()]
        result = []
        for line in lines:
            base64_string =line
            base64_bytes = base64_string.encode("ascii")
            sample_string_bytes = base64.b64decode(base64_bytes)
            sample_string = sample_string_bytes.decode("ascii")
            result.append(sample_string)
        return result
    #xcept Exception as e:
        #print(error+" Cant find help.stk | "+path+"\\Bin\\help.stk  |" + str(e))
copyright = '''© 2022 Stein#7722 - All Rights Reserved.'''
credits = ["Founder/Programmer: Stein#7722"]
#MAIN
def main():
    update()
    os.system("cls")
    os.system("mode con cols=100 lines=25")
    os.system("title STEINS TOOLKIT [STK]")
    print(Back.LIGHTRED_EX+Fore.BLACK+"STEIN'S TOOLKIT"+Back.RESET+Fore.CYAN+" v"+version+Fore.RESET+ " - "+Fore.LIGHTMAGENTA_EX+author+Fore.LIGHTYELLOW_EX+" (C) STK STEIN ALL RIGHTS RESERVED | "+Fore.RESET + path)
    print("Type 'help','copyright' or 'credits' for more information! 'exit' to exit the program")
    while True:
        print("\n")
        cmd = input(inputpre+" ").lower()
        if cmd == "help":
            print(Fore.LIGHTCYAN_EX+"------------------------------|"+Fore.LIGHTRED_EX+"HELP"+Fore.LIGHTCYAN_EX+"|------------------------------"+Fore.RESET)
            result = help()
            for line in result:
                print(line)
        elif cmd == "restart":
            os.system(f"python {path}\\main.py")
        elif cmd == "copyright":
            print(copyright)
        elif cmd == "credits":
            for user in credits:
                print(user)
        elif cmd == "exit":
            sys.exit(0)






main()





os.system("PAUSE")