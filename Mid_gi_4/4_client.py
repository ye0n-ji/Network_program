import socket
import struct

HOST = "localhost"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("1(온도) 2(습도) 3(조도) 입력: ")

    sock.sendto(msg.encode(), (HOST, PORT))

    data, _ = sock.recvfrom(1024)

    # 🔥 6바이트 → 3개 정수로 변환
    temp, humid, lumi = struct.unpack("!HHH", data)

    print(f"Temp={temp}, Humid={humid}, Lumi={lumi}")