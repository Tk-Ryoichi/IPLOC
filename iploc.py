import os
import urllib.request as urllib2
import json

print("""
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
 ^^
""")

print("""
██╗██████╗ ██╗      ██████╗  ██████╗
██║██╔══██╗██║     ██╔═══██╗██╔════╝
██║██████╔╝██║     ██║   ██║██║     
██║██╔═══╝ ██║     ██║   ██║██║     
██║██║     ███████╗╚██████╔╝╚██████╗
╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚═════╝
                                    """)

ip = input(" Ja >>>> What is your target IP: ")
url = "http://ip-api.com/json/"
response = urllib2.urlopen(url + ip)
data = response.read()
values = json.loads(data)

if "query" in values:
    print(" Ja >>>> IP: " + values["query"])
    print('')

if "city" in values:
    print(" Ja >>>> City: " + values["city"])
    print("")

if "isp" in values:
    print(" Ja >>>> ISP: " + values["isp"])
    print("")

if "country" in values:
    print(" Ja >>>> Country: " + values["country"])
    print("")

if "region" in values:
    print(" Ja >>>> Region: " + values["region"])
    print("")

if "lat" in values:
    print(" Ja >>>> Latitude " + str(values["lat"]))
    print("")

if "lon" in values:
    print(" Ja >>>> Longtitude : " + str(values["lon"]))
    print("")
    
if "regionName" in values:
    print(" Ja >>>> Region Name: " + str(values["regionName"]))
    print("")


if "timezone" in values:
    print(" Ja >>>> Timezone: " + values["timezone"])

print("""
██████╗ ██╗   ██╗ ██████╗ ████████╗███████╗ ██████╗
██╔══██╗╚██╗ ██╔╝██╔═══██╗╚══██╔══╝██╔════╝██╔════╝
██████╔╝ ╚████╔╝ ██║   ██║   ██║   █████╗  ██║     
██╔══██╗  ╚██╔╝  ██║   ██║   ██║   ██╔══╝  ██║     
██║  ██║   ██║   ╚██████╔╝   ██║   ███████╗╚██████╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝
                                                   """)

print("DISCLAIMER: Use only for educational purposes")
print("2023 © Ryotec")