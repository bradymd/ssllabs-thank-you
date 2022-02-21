#!/usr/bin/env python3
import requests, json, sys, socket, time, logging

debug=True
hostname="www.example.com"
logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) == 2:
  hostname = str(sys.argv[1])
else:
 print('requires a hostname argument')
 sys.exit()
ipAddress = socket.gethostbyname(hostname)   
url = 'https://api.ssllabs.com/api/v3/analyze?host=' + hostname + '&s=' + ipAddress + '&fromCache=on&ignoreMismatch=on&all=done'
response=requests.get(url)
j = response.json()
count=1
sleep_count= [ 60, 60, 30, 10 ]
while j['status'] == "IN_PROGRESS" or j['status'] == "DNS":
  if count < 5:
    sleep=sleep_count[count]
  else:
    sleep=10
  logging.info('host %s, status %s, sleep %s, count %d' % (hostname, j['status'],sleep, count))
  time.sleep(sleep)
  count=count+1
  response=requests.get(url)
  j = response.json()

with open(hostname + '.json', 'w') as outfile:
    outfile.write(json.dumps(j))

logging.info('writing to file %s' % (hostname + ".json"))

v = { 'hostname': "",  
        'ipAddress': "", 
        'grade': "",  
        'hasWarnings': "",  
        'isExceptional': "", 
	'heartbleed': "",
        'vulnBeast': "",
	'poodle': "",
	'freak': "",
         "logjam": "",
	"supportsRc4": "",
	"TLS" : "",
	"serverName": hostname } 

# Maybe I will find a better way of parsing this lot
v['hostname'] = hostname
v['ipAddress']  =  ipAddress
e = j['endpoints']
endpoints= e[0]
v['grade'] = endpoints['grade']
# Why does this serverName sometimes not appear?
try:
  endpoints['serverName']
except:
  endpoints['serverName'] = ""
v['serverName'] = endpoints['serverName']
v[ 'hasWarnings' ] = endpoints['hasWarnings']
v['isExceptional' ]  = endpoints[ "isExceptional" ]
details=endpoints['details']
protocols = (details['protocols'])
TLS  =  [ ]
for t in protocols:
  TLS.append(t['version'])
v['TLS'] = TLS
v['heartbleed'] = details['heartbleed']
v['vulnBeast'] = details['vulnBeast']
v['poodle'] = details['poodle']
v['freak'] = details['freak']
v['logjam'] = details['logjam']
v['supportsRc4'] = details['supportsRc4']
print(json.dumps(v,indent=4))
