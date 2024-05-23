n, m = map(int, input().split())

# 출력 포맷에 맞게 숫자 증가시켜 출력
num = 1
for i in range(n):
    for j in range(m):
        print(num, end=" ")
        num += 1
    print()  # 한 줄이 끝나면 줄바꿈