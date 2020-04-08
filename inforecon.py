import socket
import sys
import requests
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

req = requests.get('https://' + sys.argv[1])
print("\n"+str(req.headers))

gethostby = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby + "\n")

reqinfo = requests.get('https://ipinfo.io/' + gethostby + '/json')
resp    = json.loads(reqinfo.text)

print('Location: ' + resp['loc'])
print('Region: ' + resp['region'])
print('City: ' + resp['city'])
print('Country: ' + resp['country'])