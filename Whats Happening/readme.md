# Whats Happening

Author: Cyrus

Date Created/Modified: 30/5/2022

Flag: HNF{atomized}

## Description

This is the output of the cipher, can you reverse it?  
`['5', 'E', '4', 'S', '9', 'C', 'Q', '7', 'S', '3', 'C', 'Q', '0', 'N', '9', 'C', 'N', '8', 'C', 'E']`

## Hints

1. YourFirstHintHere
1. YourSecondHintHere (IF ANY)

## Distribution

These are the files that will be sent to the participants

- YourFileNameHere
  - SHA1: `YourSHA1DigestOfFileHere`
- YourSecondFileNameHere (IF ANY)
  - SHA1: `YourSHA1DigestOfFileHere`

## Solution

Looking at cipher.py
Each number represents the start of a new letter

'2' , 'C', 'G' is only obtained here
`ltr.append(str(each)[-1])
ltr.append("C")`
this means that the first letter could have a unicode of 72 or 82
It is not 72 as 72%8 = 0, hence First letter is R

'9', 'C', 'N' is again only obtained here
`ltr.append(str(each)[-1])
ltr.append("C")`
this means that the second letter could have a unicode of 69 79 89
it is not 79 or 89 as 'N' is present hence multiple of 3, hence Second Letter is E

'6', 'C', 'G' is again only obtained here
`ltr.append(str(each)[-1])
ltr.append("C")`
this means that the third letter could have a unicode of 66 76 86
It is not 66 or 76 as 66 is a multiple of 6 and 76 is a multiple of 4, hence third letter is V


