from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input("계산식 입력 (예: 20+17, 종료:q): ")

    if msg == 'q':
        s.send(msg.encode())
        break

    s.send(msg.encode())

    result = s.recv(1024).decode()
    print("결과:", result)

s.close()