import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

# 이름 전송
name = "Yeonji Kim"
sock.send(name.encode())

# 2학번 전송
data = sock.recv(4)  # int는 보통 4바이트
student_id = struct.unpack('!I', data)[0]
print(student_id)

sock.close()