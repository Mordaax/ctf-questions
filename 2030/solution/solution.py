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
        print("Index Error Lol")
    open(target_file, 'wb').write(b)


""" FF D8 FF E0 00 10 4A 46
49 46 00 01 """

xorfiles('./2030/generate/encrypted.jpg.enc',
         './2030/generate/original2.jpg', '7468697369736B65796C6F6C')


def get_key(key, message):
    key = int('0x' + key, 16)
    message = int('0x' + message, 16)
    print(hex(key ^ message))


get_key('8BB0969369632123302A6F6D', "FFD8FFE000104A4649460001")
