n = int(input())

answer = 0
if n % 5 == 0:
    print(n // 5)

else:
    while True:
        n -= 3
        if n < 0:
            print(-1)
            break
        answer += 1
        if n % 5 == 0:
            answer += n // 5
            print(answer)
            break
        else:
            continue