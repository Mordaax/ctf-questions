import base64

for i in range(1, 101):
    f = open("flag{}.txt".format(i), "r")
    b64_string = f.read()
    bytes_encoded = b64_string.encode('ascii')
    bytes_decoded = base64.b64decode(bytes_encoded)
    decoded_string = bytes_decoded.decode('ascii')
    print(decoded_string)
