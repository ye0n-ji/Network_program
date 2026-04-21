import socket
import time

HOST = "localhost"
PORT = 7000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

for _ in range(3):  # 3번 반복
    start = time.time()

    client_socket.send("ping".encode())

    data = client_socket.recv(1024)

    end = time.time()

    rtt = end - start

    print(f"Success (RTT: {rtt:.6f})")

client_socket.close()