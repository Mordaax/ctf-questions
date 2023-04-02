# Map to a secret city

Author: Cyrus Tan

Date Created/Modified: 14/10/2022

Flag: LNC2023{e279a99f2AE}

## Description

Follow the map to find the hidden treasure

## Hints

1. Coordinates

## Distribution

These are the files that will be sent to the participants

- map.txt
  - SHA1: `c170060da37089302be9520b6363e3f4bfe49cb7`

## Solution

The map contains a bunch of coordinatees

```
0x8c 0x89b
0xae 0x656
0x67 0x199
0x6a 0x9d0
0x47 0xa7e
0x7b 0x99c
0x6f 0xee6
0xaf 0x4
0xb8 0xb09
```

We can use those coordinates to plot out this series of characters

![pygamewindow](./solution/original.png)

We can then use Base 32 to decode

`JRHEGMRQGIZXWZJSG44WCOJZMYZECRL5`
