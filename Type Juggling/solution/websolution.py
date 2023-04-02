import hashlib

giventext = '2406'
password = 0

while True:
    h = hashlib.md5(bytes(giventext + str(password), 'ascii')).hexdigest()
    if h[:2] == "0e" and h[2:].isdigit():
        print(password)
        break
    password += 1
