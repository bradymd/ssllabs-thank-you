import ijson, json, sys

filename = "www.herts.ac.uk.json"

f = open(filename,'r')

data  = json.load(f)			# loads in as a dict

f.close()
print(data.keys())			# here are all the keys

print(data['host'])			# print one out
print(data.get('status'))		# and a different way 

					# this next weay searches thru the dict
if 'status' in data.keys():		# we know you are in there !
  status = [ value for key, value in data.items() if key == 'status']
  print(status.pop())			# it returns an array ( there could have been many!)

# But essentially we know status is in there as its an API so just use the simpler method data.get('status')


if 'endpoints' in data.keys():
  e = [ value for key, value in data.items() if key == 'endpoints']
  # The first POP is to get the fist array item as  this "e" value is returned as an array
  en=e[0]
  # But endpoints is an array of one item we want the dict of the first item, pop again
  end=en[0]

serverName = [ value for key, value in end.items() if key == 'serverName']
print(serverName.pop())

# But actually we know endpoints is in there so  why bother

e = data['endpoints']			# we pick out now an item in this top level called endpoints which is in fact an array

endpoints = e[0]			# we take the first item in the array  which is a dict

serverName = endpoints['serverName']	# and as its a dict it allows us to pick out a sample key - we use serverName

print(serverName)

details = endpoints['details']          # endpoints has an another item of interest  called details which is a dict

protocols = details['protocols'] 	# this dict details has an item has called protocols which is an array

status = data.get('status')

TLS  =  [ ]
for t in protocols:			# we loop thru the protocols array and take (append) each version field found
  TLS.append(t['version'])


print(status)
print(serverName)
print(TLS)
"""
can this be made any easier
"""
f = open(filename,'r')
parser=ijson.parse(f)
print(type(parser))
for prefix, event, value in parser:
  print("prefix=%s, event=%s, value=%s" % (prefix, event, value) )
#endpoints.item.details.heartbleed

f = open(filename,'r')
v = ijson.items(f, 'endpoints.item.details.heartbleed')
for h in v:
  print('heartbleed: {}'.format(h))
f = open(filename,'r')
v = ijson.items(f, 'endpoints.item.details.poodle')
for h in v:
  print('poodle: {}'.format(h))
f.close()

# Well I didn't find that easier ...

# And this not much(any) difference
f = open(filename,'r')
for k, v in ijson.kvitems(f, ''):
    # This is the top level of the JSON
    if k == 'host':
      print('host = {}'.format(v)     )
    # And this pursues the data in the endpoints array (first array item)
    if k == 'endpoints':
      newv=v.pop()
      print('ipAddress = {}'.format( newv['ipAddress']))
      print('serverName= {}'.format( newv['serverName']))  
      print('hasWarnings= {}'.format( newv['hasWarnings']))  
      print('isExceptional= {}'.format( newv['isExceptional']))  
      if details  == newv['details']:
        print('heartbeat= {}'.format(details['heartbeat']))
        print('heartbleed= {}'.format(details['heartbleed']))
        print('poodle= {}'.format(details['poodle']))
        print('vulnBeast= {}'.format(details['vulnBeast']))
        print('freak= {}'.format(details['freak']))
        print('logjam= {}'.format(details['logjam']))
        print('supportsRc4= {}'.format(details['supportsRc4']))
        protocols=details['protocols']
        TLS = []
        for t in protocols:
         TLS.append(t['version'])
        print('TLS={}'.format(TLS)) 
       


sys.exit()

