import socket
import random

port = 3333
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

print("UDP 서버 실행 중...")

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)

    # 50% 확률로 ACK 안 보냄 (손실 시뮬레이션)
    if random.random() < 0.5:
        print("[손실 발생] 메시지 무시")
        continue
    else:
        sock.sendto(b'ack', addr)
        print("<-", data.decode())