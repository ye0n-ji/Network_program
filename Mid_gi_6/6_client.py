import socket
import struct

HOST = "localhost"
PORT = 5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.send("Hello".encode())

data = client_socket.recv(1024)

sender_id, receiver_id, lumi, humi, temp, air, seq = struct.unpack('!HHBBBBI', data)

print(f"Sender:{sender_id}, Receiver:{receiver_id}, Lumi:{lumi}, "
      f"Humi:{humi}, Temp:{temp}, Air:{air}, Seq:{seq}")

client_socket.close()