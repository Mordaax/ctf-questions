import socket
import random
from threading import Thread

ServerSideSocket = socket.socket()
host = '0.0.0.0'
port = 6105
solves = 0
threads = []

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)

questionPool = {"Most popular malware type in 2021": ["adware"],
                "How many cases of cybercrime was reported in Singapore in 2019": ["9430"],
                "malicious program that provides hackers remote access over a computer of system": ["rootkit"],
                "Command to list all files including additional information like permissions": ["ls -l", "ls -la"],
                "Name of the virus used in the first ransomware attack": ["cyborg"],
                "Protocol used to establish secure links between devices over the internet": ["ssl"],
                "A network of computers infected by malware and is remotely controlled by a single party": ["botnet"],
                "Trojan used to steal banking information from windows systems": ["zeus"],
                "What type of malware is wannacry": ["ransomware"],
                "Self replicating Malware": ["worm"]}


def multi_threaded_client(connection):
    num_list = random.sample(range(7), 3)

    connection.settimeout(10)
    try:
        while True:
            for i in num_list:
                question = list(questionPool.keys())[i]
                connection.send(question.encode())
                connection.send('\n>'.encode())
                answer = connection.recv(2048)
                if (answer.decode('utf-8').strip().lower() in questionPool[question]):
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
                    "You made it here is the flag:HNF{Y0u_m4de_1t_1605}"))
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
