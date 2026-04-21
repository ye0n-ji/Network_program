from socket import *
import os
import time

HOST = 'localhost'
PORT = 6789
BUFFSIZE = 1024

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("파일 서버 실행 중...")

while True:
    data, addr = server_socket.recvfrom(BUFFSIZE)
    msg = data.decode()

    # 1. Hello 받기
    if msg == "Hello":
        server_socket.sendto(b"Filename", addr)

        # 2. 파일 이름 받기
        data, addr = server_socket.recvfrom(BUFFSIZE)
        filename = data.decode()

        if not os.path.exists(filename):
            server_socket.sendto(b"No File", addr)
            continue

        # 3. 파일 전송
        with open(filename, 'rb') as f:
            file_data = f.read()

        # 🔥 재전송 로직 (최대 3번)
        for i in range(3):
            server_socket.sendto(file_data, addr)
            print(f"파일 전송 시도 {i+1}")

            server_socket.settimeout(2)

            try:
                data, _ = server_socket.recvfrom(BUFFSIZE)
                if data.decode() == "Bye":
                    print("전송 완료")
                    break
            except:
                print("ACK 못받음 → 재전송")

        server_socket.settimeout(None)