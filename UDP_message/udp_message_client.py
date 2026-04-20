from socket import *

server_addr = ('localhost', 9999)

client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter message ("send mboxID message" or "receive mboxID" or "quit"): ')

    client_socket.sendto(msg.encode(), server_addr)

    if msg == "quit":
        break

    data, _ = client_socket.recvfrom(1024)
    print(data.decode())

client_socket.close()