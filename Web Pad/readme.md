# Web Pad

Author: Cyrus 

Date Created/Modified: 5/9/2022

Flag: GRU22{Be1l0_Aes_L3g0_bl0cks}

## Description
Part of the Vicious 6 website files have been stolen. Find a way to access the flag. They might want to recruit you
`http://ipaddress:5120`


## Setup
```
docker build -t webpad .
docker run -d -p 5120:5120 --rm -it webpad
```

## Distribution
These are the files that will be sent to the participants
- main.py
    - SHA1: `c488882184af91ddc2d05c51fe06cf02b841f176ea4e2970669f225264c29e09`

## Solution

Get Hex value of flag_user
![Hex value](./solution/hex.png)

In ECB, the plaintext is divided into blocks of the same length with the standard length of 128 for AES. AES.MODE_ECB needs to pad data until it is the same length as the block 

Goal:
Find The Encrypted value of 6d696e696f6e735f725f6177736f6d65 (We do not know the key) 
![goal](./solution/flaggoal.png)

![ECB](./solution/ecb.png)


Step 1 Figure out the Block Size 
`curl http://127.0.0.1:5120/encrypt?user=$(python3 -c "print('AA'*15)")`

`curl http://127.0.0.1:5120/encrypt?user=$(python3 -c "print('AA'*16)")`

Ciphertext length doubles with 16 pairs of `AA` indicating a 16 byte block length

Step 2 using hex value 6d696e696f6e735f725f6177736f6d65 we find that the length of user hex is 16bytes

Step3 We will pad the blocks with our own padding data, the 2nd and 3rd block will be the encrypted value of hex string 'minions_r_awsome'
```
curl http://127.0.0.1:5120/encrypt?user=$(python3 -c "print('CC'*16)")6d696e696f6e735f725
f6177736f6d65
```
Returns: 51b950b5d7e166a37adf5719e564036b`c5a653c44f17934ed8c50cc487494bbf8e64ce873f174dbb2423fcd814580e15`
```
curl http://127.0.0.1:5120/encrypt?user=$(python3 -c "print('AA'*16)")6d696e696f6e735f725
f6177736f6d65
```
Returns: cd63c85a7e82bd6f4aa28657a78e78af`c5a653c44f17934ed8c50cc487494bbf8e64ce873f174dbb2423fcd814580e15`

```
curl http://127.0.0.1:5120/encrypt?user=$(python3 -c "print('AA'*16)")6d696e696f6e735f725
f6177736f6d65
```
Returns:
82e6351d5667e7788f60360b3f124d12`c5a653c44f17934ed8c50cc487494bbf8e64ce873f174dbb2423fcd814580e15`


Step 4 Using the encrypted username we can obtain the flag
`http://127.0.0.1:5120/get_flag?user=c5a653c44f17934ed8c50cc487494bbf8e64ce873f174dbb2423fcd814580e15` 

![flag](./solution/flag.png)