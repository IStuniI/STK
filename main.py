import os
import base64

import requests


 
#functions
def install_pkg(pkg):
    os.system("pip3 install " + pkg)

#VARS
version = "0.0.1 ALPHA"
author = "Stein#7722"
update_url = ""
#BOOT
path = os.getcwd()
packages = ["colorama"]
print("Installing")
#   install the packages
for pkg in packages:
    install_pkg(pkg)
    os.system("cls")
print(path)
os.system("cls")

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
    url = requests.get

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

#MAIN
def main():
    os.system("title STEINS TOOLKIT [STK]")
    print(Back.LIGHTRED_EX+Fore.BLACK+"STEIN'S TOOLKIT"+Back.RESET+Fore.CYAN+" v"+version+Fore.RESET+ " - "+Fore.LIGHTMAGENTA_EX+author+Fore.RESET+" (C) STK STEIN ALL RIGHTS RESERVED | " + path)
    print("Type 'help','copyright' or 'credits' for more information! 'exit' to exit the program")
    while True:
        cmd = input(inputpre+" ").lower()
        if cmd == "help":
            print(Fore.LIGHTCYAN_EX+"------------------------------"+Fore.LIGHTRED_EX+"HELP"+Fore.LIGHTCYAN_EX+"------------------------------"+Fore.RESET)
            result = help()
            for line in result:
                print(line)





main()





os.system("PAUSE")