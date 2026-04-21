from socket import *

HOST = 'localhost'
PORT = 6789
BUFFSIZE = 1024

client_socket = socket(AF_INET, SOCK_DGRAM)
server_addr = (HOST, PORT)

# 1. Hello 전송
client_socket.sendto(b"Hello", server_addr)

# 2. Filename 요청 받기
data, _ = client_socket.recvfrom(BUFFSIZE)

if data.decode() == "Filename":
    filename = input("파일 이름 입력: ")

    # 3. 파일 이름 전송
    client_socket.sendto(filename.encode(), server_addr)

    # 4. 파일 받기
    data, _ = client_socket.recvfrom(BUFFSIZE)

    if data.decode() == "No File":
        print("파일 없음")
    else:
        # 파일 저장
        with open("received_" + filename, "wb") as f:
            f.write(data)

        print("파일 수신 완료")

        # 5. Bye 전송 (ACK 역할)
        client_socket.sendto(b"Bye", server_addr)

client_socket.close()