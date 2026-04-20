from socket import *
import re

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

def calculate(expr):
    # 공백 제거
    expr = expr.replace(" ", "")

    # 정규식으로 파싱 (숫자 연산자 숫자)
    match = re.match(r'^(-?\d+)([\+\-\*/])(-?\d+)$', expr)
    
    if not match:
        return "Error"

    a, op, b = match.groups()
    a = int(a)
    b = int(b)

    try:
        if op == '+':
            return str(a + b)
        elif op == '-':
            return str(a - b)
        elif op == '*':
            return str(a * b)
        elif op == '/':
            if b == 0:
                return "Error: division by zero"
            return f"{a / b:.1f}"   # 소수점 1자리
    except:
        return "Error"

while True:
    client, addr = s.accept()
    print('connection from ', addr)

    while True:
        data = client.recv(1024)

        if not data:
            break

        msg = data.decode()

        if msg == 'q':
            break

        result = calculate(msg)
        client.send(result.encode())

    client.close()