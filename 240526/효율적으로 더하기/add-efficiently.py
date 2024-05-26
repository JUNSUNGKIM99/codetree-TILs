n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
for i in range(n):
    answer += sum(arr[:i+1])
print(answer)