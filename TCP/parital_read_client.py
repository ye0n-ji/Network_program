from socket import *

sock = create_connection(('localhost', 9999))

data_size = 20 # 수신할데이터의크기
rx_size = 0
total_data = []
while rx_size < data_size:
    #최대4바이트수신하도록설정
    data = sock.recv(4)
    if not data:
        break
    
    rx_size += len(data)
    total_data.append(data.decode())
    print(total_data)
    
message = ''.join(total_data)
print(message)
sock.close()