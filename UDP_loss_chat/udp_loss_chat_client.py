import socket

port = 3333
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', port)

while True:
    msg = input("-> ")

    reTx = 0

    while reTx <= 5:
        # 재전송 번호 포함
        send_msg = str(reTx) + " " + msg

        sock.sendto(send_msg.encode(), server_addr)

        # timeout 설정 (2초)
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except socket.timeout:
            print(f"[Timeout] 재전송 {reTx+1}회")
            reTx += 1
            continue
        else:
            print("<- ack 수신")
            break