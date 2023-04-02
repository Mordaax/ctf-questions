# Hide And Seek

Author: Cyrus

Date Created/Modified: 13/6/2022

Flag: HNF{H1dIn9_1n_PL4in_5ight}

## Description
I Hide you seek

## Hints
1. YourFirstHintHere
1. YourSecondHintHere (IF ANY)

## Distribution
These are the files that will be sent to the participants
- YourFileNameHere
    - SHA1: `6e8d4ebb5864e5d2b85fa506f1b64ff163eb14d2`
- YourSecondFileNameHere (IF ANY)
    - SHA1: `YourSHA1DigestOfFileHere`

## Solution

Edit file header from 00 00 to 00 10
![File Header](/solution/File%20Header.PNG)

Extract text file using `streghide extract -f hey.jpg`

`cat flag.txt`