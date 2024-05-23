n = int(input())

# n개의 정수 입력 받기
for _ in range(n):
    num = int(input())
    if num == 0:
        print("zero")
    elif num < 0:
        print("minus")
    else:
        print("plus")