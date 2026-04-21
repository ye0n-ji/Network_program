import socket

HOST = "localhost"
PORT = 7000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("TCP Ping 서버 실행 중...")

conn, addr = server_socket.accept()
print("접속:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    msg = data.decode()

    if msg == "ping":
        conn.send("pong".encode())

conn.close()
server_socket.close()