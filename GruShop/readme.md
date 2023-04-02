# grushop

Author: Cyrus

Date Created/Modified: 6/9/2022

Flag: GRU22{b1g_numb3r}

## Description
Gru opened a new shop selling flags, find a way to break it.

`nc ipaddress 1024`

## Setup
```
docker build -t grushop .
docker run -d -p 1024:1024 --rm -it grushop
```

## Distribution
These are the files that will be sent to the participants
- Source.c
    - SHA1: `a67aaab2927a9b9f52898265dba10278c51b9de5dc05f5c76d7be5a4ef817720`

## Solution
Signed Integer overflow, supply a large quantity of fake flags for cost to be above INT_MAX, cost will be a negative number which will be credited to the user's account. User can then buy the real flag