import socket
import random
from threading import Thread

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

questionPool = {"""What is an antivirus?
1.Computer software used to prevent, detect and remove malicious software. 
2.Software used to duplicate viruses.
3.A biological agent that reproduces itself inside the cells of living things.
4.A bigger and more dangerous virus.""": "1",

                """Name a type of malware
1.Ant
2.Worms
3.Lions
4.Horses""": "2",

                """What is a trojan horse
1.A Type of horse
2.A chess piece
3.A program designed to take down the computer system while performing an inoffensive task
4.A hollow wooden statue of a horse in which the Greeks concealed themselves in order to enter Troy.""": "4",

                """What is email spoofing
1.Email messages with a forged sender address
2.Promotional Emails
3.Verification Emails
4.Adding inappropriate pictures to emails""": "1",

                """Software that enables a user to obtain secret information about another computer's activities.
1.Malware
2.Adware
3.Spyware
4.Horseware""": "3",

                """A piece of code that can copy itself and damage the system or destroy data.
1.Computer virus
2.Computer code
3.Computer hacker
4.Computer worm""": "4",
                }


def multi_threaded_client(connection):
    num_list = random.sample(range(6), 4)

    connection.settimeout(10)
    try:
        while True:
            for i in num_list:
                question = list(questionPool.keys())[i]
                connection.send(question.encode())
                connection.send('\n>'.encode())
                answer = connection.recv(2048)
                if (answer.decode('utf-8').strip().lower() == questionPool[question]):
                    connection_open = True
                    continue
                else:
                    connection.sendall(str.encode("Wrong Answer Bye"))
                    connection_open = False
                    break
            if (connection_open):
                global solves
                solves += 1
                connection.sendall(str.encode(
                    "You made it here is the flag:HNF{McQ_2_3Z_9087}"))
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
