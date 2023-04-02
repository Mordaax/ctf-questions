# Type Juggling

Author: Cyrus

Date Created/Modified: 29/5/2022

Flag: HNF{w3b_2_simple_5873}

## Description
An MD5 password hash was leaked from a web server `0e639203762320213453`, it is speculated that the all passwords look the same

## Hints
1. Admin login
2. Find a similar hash to the one above

## Setup
```docker-compose up```

## Distribution
These are the files that will be sent to the participants
- YourFileNameHere
    - SHA1: `YourSHA1DigestOfFileHere`
- YourSecondFileNameHere (IF ANY)
    - SHA1: `YourSHA1DigestOfFileHere`

## Solution
Participants must exploit the 0e PHP type juggling vulnerability

1. By trying username admin, particiapants can obtain a number 2406*****
2. Creating a python script and brute forces every number from 240600000 to 240699999 	 
3. The number 240610708 gives the hash 0e462097431906509019562988736854
4. 240610708 is the password to obtain the flag

Solution.py

```
import hashlib

giventext = '2406'
password = 0

while True:
    h = hashlib.md5(bytes(giventext + str(password), 'ascii')).hexdigest()
    if h[:2] == "0e" and h[2:].isdigit():
        print(password)
        break
    password += 1

```

Reads: https://securityaffairs.co/wordpress/36732/hacking/php-hash-comparison-flaw.html