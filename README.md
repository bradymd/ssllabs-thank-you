#  SSLLABS-THANK-YOU

## DESCRIPTION
   This python program is making use of the API v3 provided by ssllabs for analysing certificates/cipher.
   The full output is brought back in a json file, however I just pick out a few more immediately relevant items.


## TIPS on using 
```
git clone https://github.com/bradymd/ssllabs-thank-you.git
cd ssllabs-thank-you
python3 -m venv ~/.venv/ssllabs-thank-you
source ~/.ven/ssllabs-thank-you/bin/activate
pip install -r requirements.txt
```

## Example output
```
 ./ssllabs-thank-you.py www.google.com
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): api.ssllabs.com:443
DEBUG:urllib3.connectionpool:https://api.ssllabs.com:443 "GET /api/v3/analyze?host=www.google.com&s=142.250.178.4&fromCache=on&ignoreMismatch=on&all=done HTTP/1.1" 200 None
INFO:root:writing to file www.google.com.json
{
    "hostname": "www.google.com",
    "ipAddress": "142.250.178.4",
    "grade": "B",
    "hasWarnings": false,
    "isExceptional": false,
    "heartbleed": false,
    "vulnBeast": true,
    "poodle": false,
    "freak": false,
    "logjam": false,
    "supportsRc4": false,
    "TLS": [
        "1.0",
        "1.1",
        "1.2",
        "1.3"
    ],
    "serverName": "nuq04s42-in-f4.1e100.net"
}


```

