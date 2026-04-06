import socket
import re

HOST = "127.0.0.1"
PORT = 5000

def calculate_expression(expr: str) -> str:
    expr = expr.strip()

    pattern = r"^\s*(-?\d+)\s*([\+\-\*/])\s*(-?\d+)\s*$"
    match = re.match(pattern, expr)

    if not match:
        return "Error: 잘못된 계산식입니다."

    a, op, b = match.groups()
    a = int(a)
    b = int(b)

    try:
        if op == "+":
            result = a + b
            return str(result)
        elif op == "-":
            result = a - b
            return str(result)
        elif op == "*":
            result = a * b
            return str(result)
        elif op == "/":
            if b == 0:
                return "Error: 0으로 나눌 수 없습니다."
            result = a / b
            return f"{result:.1f}"
        else:
            return "Error: 지원하지 않는 연산자입니다."
    except Exception as e:
        return f"Error: {e}"


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"[서버 실행 중] {HOST}:{PORT} 에서 클라이언트 대기 중...")

    conn, addr = server_socket.accept()
    print(f"[클라이언트 연결됨] {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            expr = data.decode().strip()
            print(f"[수신] {expr}")

            if expr.lower() == "q":
                print("[서버 종료] 클라이언트가 종료를 요청했습니다.")
                break

            result = calculate_expression(expr)
            conn.sendall(result.encode())
            print(f"[전송] {result}")

    server_socket.close()
    print("서버가 종료되었습니다.")


if __name__ == "__main__":
    main()