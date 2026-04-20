# user.py
from socket import *
import time

# 디바이스 연결
d1 = socket(AF_INET, SOCK_STREAM)
d1.connect(('localhost', 9001))

d2 = socket(AF_INET, SOCK_STREAM)
d2.connect(('localhost', 9002))

print("디바이스 연결 완료")

while True:
    cmd = input("1(Device1) / 2(Device2) / quit: ")

    if cmd == '1':
        d1.send("Request".encode())
        data = d1.recv(1024).decode()

        temp, humid, illum = data.split(',')

        now = time.strftime("%a %b %d %H:%M:%S %Y")

        result = f"{now}: Device1: Temp={temp}, Humid={humid}, Illum={illum}"
        print(result)

        with open("data.txt", "a") as f:
            f.write(result + "\n")

    elif cmd == '2':
        d2.send("Request".encode())
        data = d2.recv(1024).decode()

        heart, steps, cal = data.split(',')

        now = time.strftime("%a %b %d %H:%M:%S %Y")

        result = f"{now}: Device2: Heartbeat={heart}, Steps={steps}, Cal={cal}"
        print(result)

        with open("data.txt", "a") as f:
            f.write(result + "\n")

    elif cmd == 'quit':
        d1.send("quit".encode())
        d2.send("quit".encode())
        break

d1.close()
d2.close()