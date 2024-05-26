n = int(input())
tmp = []
def solution(num):
    tmp.append(num)
    if num == 1:
        return
    else:
        if num % 2 == 0:
            return solution(num // 2)
        elif num % 2 == 1:
            return solution(num // 3)
solution(n)
for i in tmp:
    print(i, end=' ')