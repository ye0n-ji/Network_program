days = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30,
    'May': 31, 'June': 30, 'July': 31, 'August': 31,
    'September': 30, 'October': 31, 'November': 30, 'December': 31
}

# A. 알파벳 순서로 모든 월 출력
print(sorted(days.keys()))

# B. 일수 기준 오름차순 (key-value 쌍)
sorted_days = sorted(days.items(), key=lambda x: x[1])
print(sorted_days)

# C. 사용자 입력 처리
user_input = input("월 입력 (예: Jan): ")

# 3글자 → 전체 월 이름으로 변환
for month in days:
    if month.startswith(user_input):
        print(days[month])
        break