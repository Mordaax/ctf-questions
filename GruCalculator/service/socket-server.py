import socket
import random
from threading import Thread
import math

ServerSideSocket = socket.socket()
host = '0.0.0.0'
port = 5016
solves = 0
threads = []

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)


def generateQuestions():
    questions = []
    for i in range(0, 100):
        questions.append(
            {'measure': random.choice(['volume', 'area']),
             'shape': random.choice(['cube', 'sphere']),
             'number': random.randint(1, 999),
             'answer': 0
             }
        )

    for x in questions:
        if (x['measure'] == 'area'):
            if (x['shape'] == 'cube'):
                x['answer'] = math.pow(x['number'], 2)*6
            elif (x['shape'] == 'sphere'):
                x['answer'] = 12.56*math.pow(x['number'], 2)
        elif (x['measure'] == 'volume'):
            if (x['shape'] == 'cube'):
                x['answer'] = math.pow(x['number'], 3)
            elif (x['shape'] == 'sphere'):
                x['answer'] = (12.56*math.pow(x['number'], 3))/3
        x['answer'] = round(x['answer'], 2)
    return questions


def multi_threaded_client(connection):

    questions = generateQuestions()
    print(questions)

    connection.settimeout(10)
    try:
        connection.send(
            'Help Gru to pass his math exam!\n1.Use pi value of 3.14\n2.Answer to the nearst 2 decimal place\n'.encode())
        while True:
            for i in range(0, len(questions)):
                questionData = questions[i]
                question = f"Question {i+1}/100\nFind the {questionData['measure']} of {questionData['shape']} with {'radius' if questionData['shape'] == 'sphere' else 'length'} of {questionData['number']}\n>"
                connection.send(question.encode())

                answer = connection.recv(2048)
                if (float(answer.decode('utf-8').strip().lower()) == questionData['answer']):
                    connection_open = True
                    continue
                else:
                    connection.sendall(str.encode("Wrong temnswer Bye"))
                    connection_open = False
                    break
            if (connection_open):
                global solves
                solves += 1
                connection.sendall(str.encode(
                    "You made it here is the flag:GRU22{H3r35_100_M4rks}"))
                break
            else:
                break
    except socket.timeout:
        connection.send("\nYou didnt answer in time, Goodbye!\n".encode())
    connection.close()
    return


while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    thread = Thread(target=multi_threaded_client, args=(Client,))
    thread.start()
    threads.append(thread)
    print('Attempts: ' + str(len(threads)))
    print('Solves: ' + str(solves))
ServerSideSocket.close()
