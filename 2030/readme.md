# 2030

Author: Cyrus Tan

Date Created/Modified: 14/10/2022

Flag: LNC2023{w45_x0r_fun?}

## Description

A mysterious time traveller left an image of Singapore in 2030, try to decrypt it

## Hints

1. I verify its authenticity, that is my role

## Distribution

These are the files that will be sent to the participants

- flag.jpg.enc
  - SHA1: `f893e5850b66f29af7ee48d97892c94556a78cf6`

## Solution

The file given is encrypted using XOR
We can use a known plaintext attack to guess the key using the properties of XOR

```
A XOR B = C
C XOR B = A
A XOR C = B
```

The follwing is the file signature used for JPG files

`FF D8 FF E0 00 10 4A 46 49 46 00 01`

This is the first 12 bytes of the encrypted file

`8B B0 96 93 69 63 21 23 30 2A 6F 6D`

Using the following script we can obtain the key using

```
def get_key(key, message):
    key = int('0x' + key, 16)
    message = int('0x' + message, 16)
    print(hex(key ^ message))


get_key('8BB0969369632123302A6F6D', "FFD8FFE000104A4649460001")
```

Key: `7468697369736B65796C6F6C`

using the following script we can obtain the original image with the key

```
def xorfiles(source_file, target_file, key):

    key = bytearray.fromhex(key)

    b = bytearray(open(source_file, 'rb').read())
    for i in range(0, len(b), 12):
        currentbytearray = b[i:i+12]
        for x in range(0, 12):

            currentbytearray[x] ^= key[x]
        b[i:i+12] = currentbytearray

    open(target_file, 'wb').write(b)

xorfiles('encrypted.jpg.enc',
         'original.jpg', '7468697369736B65796C6F6C')

```

Finally we can find the flag in the orignal image

```
strings original.jpg | grep LNC
6\6LNC2023{w45_x0r_fun?}
```
