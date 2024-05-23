n = int(input())
numbers = list(map(int, input().split()))
accum = 0
i = 0
for num in numbers:
    accum += num
    i += 1
    if num >= 100:
        break
print(accum)
print(round(accum/i,1))