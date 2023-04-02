from logging import exception
from Crypto.Cipher import AES
from flask import Flask, request, render_template
from Crypto.Util.Padding import pad, unpad
from hidden import BLOCK_SIZE, flag, aes_key, secret_key


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = False
flag_user = 'minions_r_awsome'
flag_user = ''.join(hex(ord(c))[2:] for c in flag_user)


class AESCipher():
    def __init__(self):
        self.key = aes_key
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def encrypt(self, plaintext):
        return self.cipher.encrypt(pad(plaintext, BLOCK_SIZE)).hex()

    def decrypt(self, encrypted):
        return unpad(self.cipher.decrypt(encrypted), BLOCK_SIZE)


@app.route("/")
def main():
    return render_template('main.html', flag="Nothing here!")


@app.route("/encrypt")  # takes hex string to hex string
def encrypt():
    try:
        user = request.args.get('user')

        if user == flag_user:
            return render_template('main.html', flag="No Cheating")
        user = bytes.fromhex(user)
        return render_template('main.html', flag="Encrypted: " + AESCipher().encrypt(user))
    except:
        return render_template('main.html', flag='Something went wrong!')


@app.route("/decrypt")
def decrypt():
    user = request.args.get('user')
    user = bytes.fromhex(user)
    decryptedhexstring = AESCipher().decrypt(user).hex()
    print(decryptedhexstring)
    print(flag_user)

    return render_template('main.html', flag="Decrypted: "+AESCipher().decrypt(user).decode('utf8'))


@app.route("/get_flag")
def get_flag():
    try:
        user = request.args.get('user')
        user = bytes.fromhex(user)
        decryptedhexstring = AESCipher().decrypt(user).hex()
        if (decryptedhexstring == flag_user):
            return render_template('main.html', flag=flag)
        else:
            return render_template('main.html', flag='Invalid user!')
    except:
        return render_template('main.html', flag='Something went wrong!')


if __name__ == "__main__":
    app.run("0.0.0.0", 5120, debug=False)
