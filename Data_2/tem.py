# device1.py
from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 9001))
s.listen(1)

print("Device1 실행 중...")

while True:
    client, addr = s.accept()
    print("Device1 연결:", addr)

    while True:
        msg = client.recv(1024).decode()

        if msg == 'quit':
            break

        if msg == 'Request':
            temp = random.randint(0, 40)
            humid = random.randint(0, 100)
            illum = random.randint(70, 150)

            data = f"{temp},{humid},{illum}"
            client.send(data.encode())

    client.close()