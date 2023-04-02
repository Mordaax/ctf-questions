import socket
import math
import re

host = '127.0.0.1'
port = 5016

bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot.connect((host, port))


def evaluate(question):
    measurement = re.search("the (\w+)", question).groups(1)[0]
    shape = re.search("of (\w+)", question).groups(1)[0]
    length = int(re.findall('[0-9]+', question)[0])

    if (measurement == 'area'):
        if (shape == 'cube'):
            result = math.pow(length, 2)*6
        elif (shape == 'sphere'):
            result = 12.56*math.pow(length, 2)
    elif (measurement == 'volume'):
        if (shape == 'cube'):
            result = math.pow(length, 3)
        elif (shape == 'sphere'):
            result = (12.56*math.pow(length, 3))/3

    result = round(result, 2)
    return str(result)


for i in range(0, 100):
    try:
        data = bot.recv(1024).decode('utf8')

        question1 = data.split("\n")
        answer = evaluate(question1[-2])
    except:
        data = bot.recv(1024).decode('utf8')
        question1 = data.split("\n")
        answer = evaluate(question1[-2])
    bot.send((answer + "\n").encode())
data = bot.recv(1024).decode('utf8')
print(data)
