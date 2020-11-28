#!/usr/bin/env python3
# Author: Roman Kulich @ 2020
# Version: v1.0.0

import requests
TGREEN =  '\033[32m'
TWHITE = '\033[37m'
TRED = '\033[31m'

response = requests.get('http://cve.circl.lu/api/last')
json = response.json()

print("Last CVEs:")
for show in json:
    print(TGREEN + "CVE: " + show['id'],TWHITE)
    print(TGREEN + "Summary info: ",TWHITE + show['summary'])
    print(TGREEN + "Reference: ",TWHITE + show['references'][0])    
    print("")
