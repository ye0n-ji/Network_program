import socket
import struct
import random

HOST = "localhost"
PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("TCP 센서 서버 실행 중...")

conn, addr = server_socket.accept()
print("접속:", addr)

data = conn.recv(1024)

if data.decode() == "Hello":
    sender_id = random.randint(1, 50000)
    receiver_id = random.randint(1, 50000)

    lumi = random.randint(1, 100)
    humi = random.randint(1, 100)
    temp = random.randint(1, 100)
    air = random.randint(1, 100)

    seq = random.randint(1, 100000)

    packet = struct.pack('!HHBBBBI',
                         sender_id,
                         receiver_id,
                         lumi,
                         humi,
                         temp,
                         air,
                         seq)

    conn.send(packet)

conn.close()
server_socket.close()