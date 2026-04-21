from socket import *
import socket

HOST = 'localhost'
PORT = 9999
BUFFSIZE = 1024

client_socket = socket.socket(AF_INET, SOCK_DGRAM)
server_addr = (HOST, PORT)

while True:
    msg = input('Enter the message("send mboxID message" or "receive mboxID" or "quit"): ').strip()

    retransmit = 0
    success = False

    while retransmit <= 2:   # 최초 1회 + 재전송 2회 = 최대 3번
        client_socket.sendto(msg.encode(), server_addr)
        client_socket.settimeout(1)  # 1초 대기

        if msg == "quit":
            success = True
            break

        try:
            data, _ = client_socket.recvfrom(BUFFSIZE)
            print(data.decode())
            success = True
            break
        except socket.timeout:
            retransmit += 1
            if retransmit <= 2:
                print(f"Timeout -> 재전송 {retransmit}회")

    if msg == "quit":
        break

    if not success:
        print("응답 없음")

client_socket.close()