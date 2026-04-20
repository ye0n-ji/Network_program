import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    client.send(b'Hello ' + addr[0].encode())

    # 이름 수신
    name = client.recv(1024).decode()
    print("이름:", name)

    # 학번 전송 (문자열 변환 X, 정수를 bytes로 직접 변환)
    student_id = 20231276
    data = student_id.to_bytes(4, 'big')
    client.send(data)

    client.close()