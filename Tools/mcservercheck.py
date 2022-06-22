#Minecraft server status checker, with a lot of features.
import os
from traceback import print_tb
import requests
import json
import socket

ip = input("Enter the IP/Domain of the server: ")

url = f"https://mcapi.xdefcon.com/server/{str(ip)}/full/json"




if requests.get(url).status_code == 200:
    data = requests.get(url).text
    data = json.loads(data)
    if data["serverStatus"] == "online":
        class datas:
            data = requests.get(url).text
            data = json.loads(data)
            server_ip = data['serverip']
            server_version = data['version']
            server_motd = data['motd']["text"]
            server_players = data['players']
            server_maxplayers = data['maxplayers']
            server_ping = data['ping']
            protocol = data['protocol']
        data = requests.get(url).text
        data = json.loads(data)
        if data["serverStatus"] == "online":
            print("Server Status: " + data["serverStatus"])
            print("Server IP: " + datas.server_ip.split(":")[0])
            print("Server Version: " + datas.server_version)
            print("Server MOTD: " + datas.server_motd)
            print("Server Players: " + str(datas.server_players))
            print("Server Max Players: " + str(datas.server_maxplayers))
            print("Server Ping: " + str(datas.server_ping))
            print("Server Protocol: " + str(datas.protocol))
        print("Do you want to search open ports? (y/n)")

    else:
        print("Server is offline or server does not exist")
else:
    print("Server is offline")