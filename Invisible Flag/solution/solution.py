
puzzle = b"\r\x1d\r\r\x1d\r\r\r\r\x1d\r\r\x1d\x1d\x1d\r\r\x1d\r\r\r\x1d\x1d\r\r\x1d\x1d\x1d\x1d\r\x1d\x1d\r\x1d\r\r\r\r\x1d\x1d\r\r\x1d\x1d\r\r\r\r\r\x1d\x1d\r\x1d\x1d\r\r\r\x1d\x1d\r\x1d\x1d\r\r\r\x1d\r\x1d\x1d\x1d\x1d\x1d\r\x1d\x1d\r\x1d\x1d\r\x1d\r\r\x1d\x1d\r\r\x1d\x1d\r\x1d\r\x1d\x1d\x1d\x1d\x1d\r\x1d\r\r\x1d\x1d\r\x1d\r\r\x1d\x1d\r\x1d\r\r\r\x1d\x1d\x1d\x1d\r\r\x1d\r\r\x1d\x1d\x1d\r\r\r\r\x1d\x1d\r\r\x1d\r\x1d\r\x1d\x1d\x1d\x1d\x1d\r\x1d"
binaryflag = ""
flagArray = []
for i in range(len(puzzle)):
    x = puzzle[i]
    if x == 13:
        binaryflag += '0'
    else:
        binaryflag += '1'
    if ((i+1) % 8) == 0:
        flagArray.append(binaryflag)
        binaryflag = ""

ascii_string = ""
for binary_value in flagArray:
    an_integer = int(binary_value, 2)
    ascii_character = chr(an_integer)
    ascii_string += ascii_character

print(ascii_string)
