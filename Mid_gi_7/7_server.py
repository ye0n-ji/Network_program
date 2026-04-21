from socket import *
import random

HOST = 'localhost'
PORT = 9999
BUFFSIZE = 1024

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("UDP message 서버 실행 중...")

mailbox = {}   # {mboxID: [msg1, msg2, ...]}

while True:
    data, addr = server_socket.recvfrom(BUFFSIZE)
    msg = data.decode().strip()

    print("수신:", msg)

    # quit
    if msg == "quit":
        print("서버 종료")
        break

    # 25% 확률로 응답 안 함
    if random.random() < 0.25:
        print("응답 손실 발생")
        continue

    parts = msg.split()

    # send [mboxID] message
    if len(parts) >= 3 and parts[0] == "send":
        mboxID = parts[1]
        message = " ".join(parts[2:])

        if mboxID not in mailbox:
            mailbox[mboxID] = []

        mailbox[mboxID].append(message)
        server_socket.sendto(b"OK", addr)

    # receive [mboxID]
    elif len(parts) == 2 and parts[0] == "receive":
        mboxID = parts[1]

        if mboxID in mailbox and len(mailbox[mboxID]) > 0:
            response = mailbox[mboxID].pop(0)
            server_socket.sendto(response.encode(), addr)
        else:
            server_socket.sendto(b"No messages", addr)

    else:
        server_socket.sendto(b"Invalid command", addr)

server_socket.close()