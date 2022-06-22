#checking server from a hoster named gamesrapid
import requests
import json

node_1 = "162.55.129.242"
node_2 =  "45.142.183.58"
node_3 = "176.9.46.245"
print("1 " + node_1)
print("2 " + node_2)
print("3 " + node_3)
which = input("Which node do you want to use? enter 0 to custom >>> ")
if which == "0":
    ip = input("Enter the IP/Domain of the server without port: ")
elif which == "1":
    ip = node_1
elif which == "2":
    ip = node_2
elif which == "3":
    ip = node_3
else:
    print("No valid option!")
    exit(0)
portbegin = input("Enter the begin port: ")
while True:
    portbegin = int(portbegin)
    portbegin += 1
    print("Scanning port: "+str(portbegin))
    url = f"https://mcapi.xdefcon.com/server/{str(ip)}:{str(portbegin)}/full/json"
    if requests.get(url).status_code == 200:
        data = requests.get(url).text
        data = json.loads(data)
        if data["serverStatus"] == "online":
            print(f"[+] > Port {portbegin} is open!")
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
                print("")
                print("Server Status: " + data["serverStatus"])
                print("Server IP: " + datas.server_ip.split(":")[0])
                print("Server Version: " + datas.server_version)
                print("Server MOTD: " + datas.server_motd)
                print("Server Players: " + str(datas.server_players))
                print("Server Max Players: " + str(datas.server_maxplayers))
                print("Server Ping: " + str(datas.server_ping))
                print("Server Protocol: " + str(datas.protocol))
                discord_webhook_url = 'https://canary.discord.com/api/webhooks/988851696966971475/56dxNlOji-KXcxFKRvqsPUWq3ZBh3nNT3GtfCOTGg5Hz81Jhx7HuK0HWkqYIAxfMz9zT'
                Message = {
                    "content": f"SERVER FOUND, IP: {datas.server_ip} VERSION:{datas.server_version} MAXPLAYERS: {datas.server_maxplayers} [ @everyone ]"
                }
                requests.post(discord_webhook_url, data=Message)
                print("")
        else:
            pass
    else:
        pass
    