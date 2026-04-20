from socket import *

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('localhost', 9999))

print("UDP 서버 실행 중...")

mailbox = {}  # {mboxID: [msg1, msg2, ...]}

while True:
    data, addr = server_socket.recvfrom(1024)
    msg = data.decode()

    print("수신:", msg)

    parts = msg.split()

    if parts[0] == "send":
        mboxID = parts[1]
        message = " ".join(parts[2:])  # 여러 단어 가능

        if mboxID not in mailbox:
            mailbox[mboxID] = []

        mailbox[mboxID].append(message)

        server_socket.sendto("OK".encode(), addr)

    elif parts[0] == "receive":
        mboxID = parts[1]

        if mboxID in mailbox and len(mailbox[mboxID]) > 0:
            message = mailbox[mboxID].pop(0)
            server_socket.sendto(message.encode(), addr)
        else:
            server_socket.sendto("No messages".encode(), addr)

    elif parts[0] == "quit":
        print("서버 종료")
        break

server_socket.close()