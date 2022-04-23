import json
import urllib.request
path = r"input.json"
newData = []
with open(path) as file:
    data = json.load(file)
for i in data:
    if 'ssl.handshake.extensions_server_name' in str(i["_source"]["layers"]):
        newData.append(i)
baseUrl = "https://geo.ipify.org/api/v2/country,city,vpn?apiKey=API_KEY&ipAddress="
for i in newData:
    finalUrl = baseUrl + i["_source"]["layers"]["ip.dst"][0]
    print(finalUrl)
    with urllib.request.urlopen(finalUrl) as url:
        data = json.loads(url.read().decode())
        print(data)
