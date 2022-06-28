import os
import base64
import sys
from time import sleep
import requests

 
#functions

def install_pkg(pkg):
    os.system("pip3 install " + pkg)
    os.system("cls")
    os.system("python3 -m pip install " + pkg)
def check_setting(setting):
    with open("C:\\STK\\bin\\STK\\asset\\settings.stk", "rb") as f:
        lines = [x.decode('utf8').strip() for x in f.readlines()]
        for line in lines:
            if setting in line:
                line.split("=")[1]
                return line.split("=")[1].lower()
#VARS
author = "Stein#7722"
update_url = "https://raw.githubusercontent.com/IStuniI/STK/main/asset/version.stk"
#BOOT
path = "C:\STK\\bin\STK"
packages = ["colorama"]
print("Installing")
#   install the packages
if not check_setting("fastboot") == "true":
    for pkg in packages:
        install_pkg(pkg)
        os.system("cls")
    print(path)
os.system("cls")
version = open(path+"\\asset\\version.stk", "r").read().split("\n")[0]
def check_tos():
    if os.path.isfile("C:\\STK\\bin\\STK\\contract.stk"):
        with open("C:\\STK\\bin\\STK\\contract.stk", "rb") as f:
            lines = [x.decode('utf8').strip() for x in f.readlines()]
            #check last line
            if lines[-1].split(":")[1].lower() == "true":
                return True
    else:
        print(error+" Cant find contract.stk")
        return False


 
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
found_pre = Fore.LIGHTCYAN_EX+"["+Fore.LIGHTMAGENTA_EX+"#"+Fore.LIGHTCYAN_EX+"]"+Fore.RESET+" "


#built-in commands
if not check_tos():
    print(error+" You have to accept the terms of service!")
    print(error+" Please accept the terms of service by typing 'accept:true' in the file 'asset\\contract.stk'")
    sys.exit()
def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, Fore.LIGHTGREEN_EX+"#"*x, Fore.CYAN+"."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

def update():
    url = requests.get(update_url)
    if url.status_code == 200:
        os.system("cls")
        print(succes+" Checking for updates...")
        if version != url.text.split("\n")[0]:
            print(succes+" Update found! New version: "+url.text + "You are running version: "+version)
            print("Do you want to update? (y/n)")
            cmd = input(inputpre+" ").lower()
            if cmd == "y":
                try:
                    os.system("cls")
                    print(succes+" Downloading...")
                    print(succes+" Cleaning...")
                    os.system("rmdir /S /Q C:\STK\\bin\STK")
                    os.system("del /f /s /q C:\STK\\bin\STK")
                    os.system("git clone https://github.com/IStuniI/STK.git C:\STK\\bin\STK")
                    os.system("cls")
                    os.system("cls")
                    print(succes+" Cloned! Cleaning up...")
                    os.system("cls")
                    os.system("cls")
                    print(succes+" Successfully updated! Restarting...")
                    os.system(f"python3 {path}\\main.py")
                    os.system("cls")
                except:
                    print(error+" Error while updating!Please try again later!")

            elif cmd == "n":
                print(succes+" Not updating...")
        else:
            print(succes+" No updates found!")
        
    else:
        print(error+" Update failed!")
def help():
    #try: 
    with open(path+"\\asset\\help.stk", "rb") as f:
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
    if not check_setting("fastboot") == "true":
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
        elif cmd == "discord":
            os.system("start https://discord.gg/vxRvsjZ537")
        elif cmd == "update":
            update()
        elif cmd == "load":
            for i in progressbar(range(100), Fore.LIGHTCYAN_EX+"Loading: "+Fore.CYAN, 40):
                sleep(0.1)
        elif cmd == "clear":
            os.system("cls")
        elif cmd == "cls":
            os.system("cls")
        elif cmd.startswith("encrypt"):
            cmd = cmd.split(" ")
            if not len(cmd) >= 2:
                print(waiting+" Usage: encrypt <de/en crypt> <text or file> ")
            else:
                if check_setting("openexternwindow") == "true":
                    try:
                        os.system(f"start {path}\\asset\\encryptor.py {cmd[1]} {cmd[2]}")
                    except KeyboardInterrupt:
                        main()
                else:
                    try:
                        os.system(f"python {path}\\asset\\encryptor.py {cmd[1]} {cmd[2]}")
                    except KeyboardInterrupt:
                        main()

        elif cmd == "stknetwork":
            if check_setting("openexternwindow") == "true":
                try:
                    os.system(f"start {path}\\asset\\stknetwork.py")
                except KeyboardInterrupt:
                    main()
            else:
                try:
                    os.system(f"python {path}\\asset\\stknetwork.py")
                except KeyboardInterrupt:
                    main()




        elif cmd == "tools":
            print(Fore.LIGHTCYAN_EX+"------------------------------|"+Fore.LIGHTRED_EX+"TOOLS"+Fore.LIGHTCYAN_EX+"|------------------------------"+Fore.RESET)
            tools = os.listdir(path+"\\Tools")
            for tool in tools:
                if not os.path.isdir(path+"\\Tools\\"+tool):
                    try:
                        if open(path+"\\Tools\\"+tool, "r").read().split("\n")[0].startswith("#"):
                            desc = open(path+"\\Tools\\"+tool, "r").read().split("\n")[0].replace("#", "")
                            print(found_pre+tool.split(".")[0] +" - "+desc)
                    except:
                        pass


        elif cmd.startswith("cmd:"):
            cmd = cmd.replace("cmd:", "")
            os.system(cmd)
        else:
            if os.path.exists(path+"\\Tools\\"+cmd+".py"):
                if check_setting("openexternwindow") == "true":
                    try:
                        os.system(f"start {path}\\Tools\\{cmd}.py")
                    except KeyboardInterrupt:
                        main()
                else:
                    try:
                        os.system(f"python {path}\\Tools\\{cmd}.py")
                    except KeyboardInterrupt:
                        main()
            else:
                print(error+" Unknown command!")





try:
    main()
except KeyboardInterrupt:
    print(error+" KeyboardInterrupt!")
    sleep(1)
    main()

os.system("PAUSE")