
def xorfiles(source_file, target_file, key):

    key = bytearray.fromhex(key)

    b = bytearray(open(source_file, 'rb').read())
    try:
        for i in range(0, len(b), 12):
            currentbytearray = b[i:i+12]
            for x in range(0, 12):

                currentbytearray[x] ^= key[x]
            b[i:i+12] = currentbytearray
    except IndexError:
        print("Index Error edit file")
    open(target_file, 'wb').write(b)


""" FF D8 FF E0 00 10 4A 46
49 46 00 01 """

xorfiles('./2.Hexor/generate/original.jpg',
         './2.Hexor/generate/encrypted.jpg.enc', '7468697369736B65796C6F6C')
