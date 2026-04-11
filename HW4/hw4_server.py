from socket import *
import os

HOST = "127.0.0.1"
PORT = 80


def get_mime_type(filename):
    if filename.endswith(".html"):
        return "text/html; charset=utf-8"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".ico"):
        return "image/x-icon"
    else:
        return "text/plain"


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

print(f"웹 서버 실행 중: http://{HOST}:{PORT}/index.html")

while True:
    client_socket, addr = server_socket.accept()
    print("접속:", addr)

    data = client_socket.recv(1024)
    request = data.decode(errors="ignore")
    print("요청 메시지:\n", request)

    lines = request.split("\r\n")
    if len(lines) == 0 or lines[0] == "":
        client_socket.close()
        continue

    request_line = lines[0]
    parts = request_line.split()

    if len(parts) < 2:
        client_socket.close()
        continue

    path = parts[1]          
    filename = path.lstrip("/")

    if filename == "":
        filename = "index.html"

    if os.path.exists(filename):
        mime_type = get_mime_type(filename)

        header = "HTTP/1.1 200 OK\r\n"
        header += f"Content-Type: {mime_type}\r\n"
        header += "\r\n"

        client_socket.send(header.encode())

        if filename.endswith(".html"):
            with open(filename, "r", encoding="utf-8") as f:
                body = f.read()
            client_socket.send(body.encode("utf-8"))
        else:
            with open(filename, "rb") as f:
                body = f.read()
            client_socket.send(body)

    else:
        header = "HTTP/1.1 404 Not Found\r\n"
        header += "Content-Type: text/html; charset=utf-8\r\n"
        header += "\r\n"

        body = "<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>"

        client_socket.send(header.encode())
        client_socket.send(body.encode("utf-8"))

    client_socket.close()