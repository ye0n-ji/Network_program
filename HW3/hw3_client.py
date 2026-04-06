import socket

HOST = "127.0.0.1"
PORT = 5000

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("TCP 계산기 클라이언트")
    print("계산식을 입력하세요. 예: 20+17, 20 - 3, 4*5, 10/3")
    print("종료하려면 q 입력")

    while True:
        expr = input("입력 > ").strip()

        if not expr:
            print("빈 입력은 허용되지 않습니다.")
            continue

        client_socket.sendall(expr.encode())

        if expr.lower() == "q":
            print("클라이언트를 종료합니다.")
            break

        result = client_socket.recv(1024).decode()
        print("결과 :", result)

    client_socket.close()


if __name__ == "__main__":
    main()