import socket
import struct
import random

HOST = "localhost"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("IoT UDP 서버 실행 중...")

while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode().strip()

    temp = 0
    humid = 0
    lumi = 0

    if msg == "1":
        temp = random.randint(1, 50)
    elif msg == "2":
        humid = random.randint(1, 100)
    elif msg == "3":
        lumi = random.randint(1, 150)

    # 🔥 2바이트씩 3개 → 총 6바이트
    packet = struct.pack("!HHH", temp, humid, lumi)

    sock.sendto(packet, addr)