# device2.py
from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 9002))
s.listen(1)

print("Device2 실행 중...")

while True:
    client, addr = s.accept()
    print("Device2 연결:", addr)

    while True:
        msg = client.recv(1024).decode()

        if msg == 'quit':
            break

        if msg == 'Request':
            heart = random.randint(40, 140)
            steps = random.randint(2000, 6000)
            cal = random.randint(1000, 4000)

            data = f"{heart},{steps},{cal}"
            client.send(data.encode())

    client.close()